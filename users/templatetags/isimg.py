from django import template

register = template.Library()

@register.filter
def isimg(file_path):
    file_path = str(file_path)
    if file_path.split(".")[-1].lower() in ["jpg", "jpeg", "tiff", "bmp", "png", "gif"]:
        return True
    else:
        return False