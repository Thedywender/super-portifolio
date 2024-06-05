from rest_framework import serializers
from .models import Profile, Project, CertifyingInstitution, Certificate
from django.contrib.auth import get_user_model

User = get_user_model()

from django.db.models import Q
from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    ValidationError,
)


class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField(
        label="Código do Usuário", allow_blank=True, required=False
    )

    class Meta:
        model = User
        fields = ["username", "password", "token"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        user_obj = None
        username = data.get("username", None)
        password = data["password"]
        if not username:
            raise ValidationError("Insira o Código de Usuário!")

        user = User.objects.filter(Q(username=username)).distinct()
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("Esse Código de Usuário não é válido!")

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Credenciais Incorretas!")

            data["token"] = "Some token Here"

        return data


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class NestedCertifyingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ["id", "name"]


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = "__all__"


class CertifyingInstitutionSerializer(serializers.ModelSerializer):
    certificates = NestedCertifyingSerializer(many=True)

    class Meta:
        model = CertifyingInstitution
        fields = ["id", "name", "url", "certificates"]

    def create(self, data):
        certificates = data.pop("certificates", [])
        certifying_institution = CertifyingInstitution.objects.create(**data)
        for certificate in certificates:
            Certificate.objects.create(
                certifying_institution=certifying_institution, **certificate
            )
        return certifying_institution
