from django.conf.urls import url
from core.views import UserListView, ProfileUpdateView, ProfileView, BashView, BashOutputView

urlpatterns = [
    url(r'^bash/', BashView.as_view(), name='bash'),
    url(r'^bash_output/(?P<output>[\w\-\n\r,: ]+)', BashOutputView.as_view(), name='bash_output'),
    url(r'^users/', UserListView.as_view(), name='user_list'),
    url(r'^profile/update/(?P<pk>.+)', ProfileUpdateView.as_view(), name='user_update'),
    url(r'^profile/(?P<pk>.+)', ProfileView.as_view(), name='user_detail'),
]
