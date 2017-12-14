from django.conf.urls import url
from core.views import UserListView, ProfileUpdateView, ProfileView

urlpatterns = [
    url(r'^users/', UserListView.as_view(), name='user_list'),
    url(r'^profile/(?P<pk>.+)', ProfileView.as_view(), name='user_detail'),
    url(r'^profile/update/(?P<pk>.+)', ProfileUpdateView.as_view(), name='user_update'),
]
