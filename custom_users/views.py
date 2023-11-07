from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView
from . import forms, models
from django.shortcuts import render


class AuthLogoutView(LogoutView):
    next_page = reverse_lazy('users:home')


class RegistrationView(CreateView):
    form_class = forms.CustomRegisterForm
    success_url = '/users/'
    template_name = 'users/register.html'


class AuthLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse('users:post')


class UserListView(ListView):
    queryset = User.objects.all()
    template_name = 'users/homepage.html'

    def get_queryset(self):
        return User.objects.all()

def staffView(request):
    staff_value = models.Staff.objects.all()
    context = {
        'post_key': staff_value,
    }
    return render(request, 'users/staff.html', context)