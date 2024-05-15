from django.db import models
from .validators import validate_not_empty, validate_max_length
from django.contrib.auth.models import AbstractUser, Group, Permission


class UserModel(AbstractUser):
    name = models.CharField(
        max_length=30, validators=[validate_not_empty], unique=True
    )
    email = models.EmailField(
        validators=[validate_not_empty, validate_max_length], unique=True
    )

    groups = models.ManyToManyField(Group, related_name="usermodel_set")
    user_permissions = models.ManyToManyField(
        Permission, related_name="usermodel_set"
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)
        if is_new:
            profile = Profile.objects.create(user=self, name=self.name)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    name = models.CharField(
        max_length=100, validators=[validate_not_empty, validate_max_length]
    )
    github = models.URLField(
        validators=[validate_not_empty, validate_max_length]
    )
    linkedin = models.URLField(
        validators=[validate_not_empty, validate_max_length]
    )
    bio = models.TextField(
        validators=[validate_not_empty, validate_max_length]
    )

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(
        max_length=50, validators=[validate_not_empty, validate_max_length]
    )
    description = models.TextField(
        max_length=500,
        validators=[validate_not_empty, validate_max_length],
    )
    github_url = models.URLField(
        validators=[validate_not_empty, validate_max_length]
    )
    keyword = models.CharField(
        max_length=50, validators=[validate_not_empty, validate_max_length]
    )
    key_skill = models.CharField(
        max_length=50, validators=[validate_not_empty, validate_max_length]
    )
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="projects"
    )

    def __str__(self):
        return self.name


class CertifyingInstitution(models.Model):
    name = models.CharField(
        max_length=100, validators=[validate_not_empty, validate_max_length]
    )
    url = models.URLField(validators=[validate_not_empty, validate_max_length])

    def __str__(self):
        return self.name


class Certificate(models.Model):
    name = models.CharField(
        max_length=100, validators=[validate_not_empty, validate_max_length]
    )
    certifying_institution = models.ForeignKey(
        CertifyingInstitution,
        on_delete=models.CASCADE,
        related_name="certificates",
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    profiles = models.ManyToManyField(Profile, related_name="certificates")

    def __str__(self):
        return self.name
