
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from notification.consumers import NotificationConsumer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('notification.urls')),

]
websocket_urlpatterns = [
    path("ws/notifications/", NotificationConsumer.as_asgi())
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
