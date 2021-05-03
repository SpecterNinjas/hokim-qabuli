from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

# urlpatterns = i18n_patterns(
#
#
# )
urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('panel/', include('panel.urls')),
   # url('bot/', include(u'telegrambot.urls')),
)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
