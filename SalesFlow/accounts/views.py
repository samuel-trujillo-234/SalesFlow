from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomAuthenticationForm

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'accounts/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'accounts/logged_out.html'

class CustomUserCreateView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')


