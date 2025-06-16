from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password')

class CustomPasswordResetForm(PasswordResetForm):
    class Meta:
        model = CustomUser
        fields = ('email',)
