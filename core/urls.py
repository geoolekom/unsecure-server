from django.conf.urls import url
from core.views import UserListView

urlpatterns = [
    url(r'^users/', UserListView.as_view(), name='user_list'),
]