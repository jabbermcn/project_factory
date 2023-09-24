from django.urls import path, include

from api import views
from api.views import UserViewSet

urlpatterns = [
    path('register/', UserViewSet.as_view({'post': 'create'}), name='user-create'),
    path('auth/', include('rest_authtoken.urls')),
    path('send_message/', views.send_message, name='send_message'),
    path('get_messages/', views.get_messages, name='get_messages'),
]
