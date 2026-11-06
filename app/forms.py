from django import forms
from django.contrib.auth.forms import(
    UserCreationForm,
    AuthenticationForm,   
)
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
        ]

class loginForm(AuthenticationForm):
    username = forms.CharField(max_length=67)
    password = forms.CharField(
        widget=forms.PasswordInput
    )