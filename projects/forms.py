from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

User = get_user_model()


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


# class LoginForm(AuthenticationForm):
#     username = forms.EmailField(
#         widget=forms.TextInput(attrs={"autofocus": True})
#     )
