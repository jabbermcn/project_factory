import os
import telebot
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Message
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_message(request):
    bot = telebot.TeleBot(os.getenv('BOT_TOKEN'))
    text = request.data.get('text')
    message = Message.objects.create(user=request.user, text=text)
    chat_id = os.getenv('BOT_GROUP_ID')
    text = f'{request.user.username}, я получил от тебя сообщение:\n{text}'
    bot.send_message(chat_id=chat_id, text=text)
    return Response({'detail': 'Сообщение отправлено'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_messages(request):
    messages = Message.objects.filter(user=request.user).values('date', 'text')
    return Response(messages)
