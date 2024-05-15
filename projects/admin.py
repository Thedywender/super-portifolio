from django.contrib import admin
from .models import (
    Profile,
    Project,
    CertifyingInstitution,
    Certificate,
    UserModel,
)

admin.site.register(UserModel)
admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(CertifyingInstitution)
admin.site.register(Certificate)

# Register your models here.
