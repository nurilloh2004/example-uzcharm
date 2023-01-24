from django import template
from users.models import Message

register = template.Library()

@register.filter
def count_unread(user):
    return Message.objects.filter(seen=False, sender=user).count()