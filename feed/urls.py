from django.conf.urls import url
from feed.views import PostView

urlpatterns = [
    url(r'post/(?P<pk>\d+)', PostView.as_view(), name='post_detail')
]
