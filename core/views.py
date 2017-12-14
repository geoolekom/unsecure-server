from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, FormView, TemplateView
from core.forms import BashForm


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
    model = User

    def get_object(self, queryset=None):
        users = User.objects.raw('SELECT * FROM auth_user WHERE id = {0}'.format(self.kwargs.get('pk')))
        count = 0
        for _ in users:
            count += 1
        if count:
            user = users[0]
        else:
            user = None

        if not user:
            raise Http404('Не найдено')
        elif user.id != self.request.user.id:
            raise PermissionDenied('Вы - не этот пользователь')
        else:
            return user


class ProfileUpdateView(UpdateView):
    model = User
    fields = '__all__'
    success_url = reverse_lazy('core:user_list')

    def get_object(self, queryset=None):
        user = super(ProfileUpdateView, self).get_object(queryset=queryset)
        if user.id != self.request.user.id:
            raise PermissionDenied('Вы - не этот пользователь')
        return user


class BashView(FormView):
    form_class = BashForm
    template_name = 'core/bash.html'
    output = None
    
    def form_valid(self, form):
        input = form.cleaned_data.get('input')
        import subprocess
        self.output = subprocess.run(input.split(), stdout=subprocess.PIPE).stdout.decode()
        self.output = ','.join(self.output.split('\n'))
        return super(BashView, self).form_valid(form)

    def get_success_url(self):
        return reverse('core:bash_output', kwargs={'output': self.output})


class BashOutputView(TemplateView):
    template_name = 'core/bash_output.html'

    def get_context_data(self, **kwargs):
        context = super(BashOutputView, self).get_context_data(**kwargs)
        context['output'] = self.kwargs.get('output')
        return context
