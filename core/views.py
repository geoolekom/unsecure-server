from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView


class UserListView(ListView):
    http_method_names = ['get']
    model = User
    fields = None

    def dispatch(self, request, *args, **kwargs):
        self.fields = ['username']
        if 'fields' in request.GET:
            fields = request.GET.get('fields')
            for field in fields.split(','):
                if hasattr(User, field):
                    self.fields.append(field)
        return super(UserListView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return super(UserListView, self).get_queryset().values(*self.fields)

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['fields'] = self.fields
        return context


class ProfileView(DetailView):

    def get_object(self, queryset=None):
        return User.objects.raw('SELECT * FROM auth_user WHERE id = {0}'.format(self.request.user.id))

