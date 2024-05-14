# Generated by Django 4.2.3 on 2024-05-14 14:46

from django.db import migrations, models
import django.db.models.deletion
import projects.validators


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CertifyingInstitution",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        validators=[
                            projects.validators.validate_not_empty,
                            projects.validators.validate_max_length,
                        ],
                    ),
                ),
                (
                    "url",
                    models.URLField(
                        validators=[
                            projects.validators.validate_not_empty,
                            projects.validators.validate_max_length,
                        ]
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        validators=[
                            projects.validators.validate_not_empty,
                            projects.validators.validate_max_length,
                        ],
                    ),
                ),
                (
                    "github",
                    models.URLField(
                        validators=[
                            projects.validators.validate_not_empty,
                            projects.validators.validate_max_length,
                        ]
                    ),
                ),
                (
                    "linkedin",
                    models.URLField(
                        validators=[
                            projects.validators.validate_not_empty,
                            projects.validators.validate_max_length,
                        ]
                    ),
                ),
                (
                    "bio",
                    models.TextField(
                        validators=[
                            projects.validators.validate_not_empty,
                            projects.validators.validate_max_length,
                        ]
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=30,
                        validators=[projects.validators.validate_not_empty],
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254,
                        validators=[
                            projects.validators.validate_not_empty,
                            projects.validators.validate_max_length,
                        ],
                    ),
                ),
                (
                    "password",
                    models.CharField(
                        max_length=20,
                        validators=[projects.validators.validate_not_empty],
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=50,
                        validators=[
                            projects.validators.validate_not_empty,
                            projects.validators.validate_max_length,
                        ],
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        max_length=500,
                        validators=[
                            projects.validators.validate_not_empty,
                            projects.validators.validate_max_length,
                        ],
                    ),
                ),
                (
                    "github_url",
                    models.URLField(
                        validators=[
                            projects.validators.validate_not_empty,
                            projects.validators.validate_max_length,
                        ]
                    ),
                ),
                (
                    "keyword",
                    models.CharField(
                        max_length=50,
                        validators=[
                            projects.validators.validate_not_empty,
                            projects.validators.validate_max_length,
                        ],
                    ),
                ),
                (
                    "key_skill",
                    models.CharField(
                        max_length=50,
                        validators=[
                            projects.validators.validate_not_empty,
                            projects.validators.validate_max_length,
                        ],
                    ),
                ),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="projects",
                        to="projects.profile",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="profile",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                to="projects.usermodel",
            ),
        ),
        migrations.CreateModel(
            name="Certificate",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        validators=[
                            projects.validators.validate_not_empty,
                            projects.validators.validate_max_length,
                        ],
                    ),
                ),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "certifying_institution",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="certificates",
                        to="projects.certifyinginstitution",
                    ),
                ),
                (
                    "profiles",
                    models.ManyToManyField(
                        related_name="certificates", to="projects.profile"
                    ),
                ),
            ],
        ),
    ]
