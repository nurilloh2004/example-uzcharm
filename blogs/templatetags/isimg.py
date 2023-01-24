import os
from django import template

register = template.Library()

@register.filter
def isimg(value):
    return os.path.basename(value.file.name).split(".")[-1].lower() in ["jpg", "jpeg", "gif", "png", "bmp"]