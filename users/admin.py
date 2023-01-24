from django.contrib import admin
from django.contrib.auth import get_user_model
import admin_thumbnails
from django.db import models

from .models import Message


class MessageAdmin(admin.ModelAdmin):
    pass


class MessageInline(admin.StackedInline):
    model = Message
    fields = ["text", "attachment"]
    readonly_fields = ["text", "attachment"]
    fk_name = "sender"
    extra = 0

User = get_user_model()

@admin_thumbnails.thumbnail("organization_charter")
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ("password",)
    inlines = [MessageInline]


admin.site.register(User, UserAdmin)
admin.site.register(Message, MessageAdmin)