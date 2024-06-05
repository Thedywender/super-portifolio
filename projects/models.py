from django.db import models
from .validators import validate_not_empty, validate_max_length
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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
