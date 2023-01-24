from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from blogs.views import index_page

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('blogs.urls')),
    path('user/', include('users.urls')),
)

urlpatterns.append(path("", index_page))

urlpatterns += [
    path('rosetta/', include('rosetta.urls')),
    # path('captcha/', include('captcha.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

handler500 = 'blogs.views.error_500'
handler404 = 'blogs.views.error_404'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# admin.site.site_header = _('Uzcharmsanoat admin panel')
# admin.site.site_title = _('Uzcharmsanoat Admin Portal')
# admin.site.index_title = _('Welcome to Uzcharmsanoat Portal')
