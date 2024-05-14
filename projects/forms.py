from django.forms import ModelForm
from .models import UserModel as User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = "__all__"
