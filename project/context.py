from blogs import models
from django.db.models import Q


def find_parent(request):
    path = str(request.path)
    sub_path = path.split("/")[-2] + "/"
    shortlink = models.ShortLink.objects.filter(url=sub_path).first()
    try:
        if shortlink.parent:
            return shortlink.parent
        else:
            return None
    except:
        return None



def defaults(req):
    return {
        "menus": models.Menu.objects.filter(parent__isnull=True),
        "menu_settings": models.MenuSettings.objects.first(),
        "regions": models.Region.objects.all(),
        "tashkent": models.Region.objects.filter(Q(translations__name__contains="kent") & Q(translations__name__contains="shahar")).first(),
        "menu_links": models.MenuOverlay.objects.filter(),
        "banners": models.Banner.objects.filter(),
        "tuts_parent": find_parent(req)
    }
