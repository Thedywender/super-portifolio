from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Project, CertifyingInstitution, Certificate

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


class CertifyingInstitutionForm(forms.ModelForm):
    class Meta:
        model = CertifyingInstitution
        fields = "__all__"


class CertificateForm(forms.ModelForm):
    certifying_institution = forms.ModelChoiceField(
        queryset=CertifyingInstitution.objects.all(),
        label="Certifying Institution",
        help_text="Select the certifying institution.",
    )

    class Meta:
        model = Certificate
        fields = ["name", "certifying_institution"]
