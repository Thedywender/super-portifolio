from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Project

User = get_user_model()


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["name", "github", "linkedin", "bio"]


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["name", "description", "github_url", "keyword", "key_skill"]
