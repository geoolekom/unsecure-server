from django.conf.urls import url
from core.views import UserListView, ProfileUpdateView

urlpatterns = [
    url(r'^users/', UserListView.as_view(), name='user_list'),
    url(r'^profile/update/(?P<pk>\d+)', ProfileUpdateView.as_view(), name='user_update'),
]
