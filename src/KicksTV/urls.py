from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from .views import index


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^gallery/', include('gallery.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^$', index, name="index")
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
