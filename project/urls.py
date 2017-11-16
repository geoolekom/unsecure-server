from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^core/', include('core.urls', namespace='core')),
    url(r'^feed/', include('feed.urls', namespace='feed')),
]
