from django import template

register = template.Library()

@register.filter
def last_wildcard(request):
    splitted = request.path.split("/")

    if len(splitted) > 1:
        return int(splitted[-1])
    else:
        return None