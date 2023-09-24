from django.contrib import admin

from api.models import Message


@admin.register(Message)
class ContactAdmin(admin.ModelAdmin):
    pass
