# Generated by Django 4.2.3 on 2024-06-25 16:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0002_alter_profile_user_delete_usermodel"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="photo",
            field=models.ImageField(
                blank=True, null=True, upload_to="Profile_photo/"
            ),
        ),
    ]
