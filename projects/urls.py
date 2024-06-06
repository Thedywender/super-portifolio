from rest_framework import routers
from .views import ProfileViewSet
from django.urls import path, include
from .views import (
    ProfileViewSet,
    ProjectViewSet,
    CertifyingInstitutionViewSet,
    CertificateViewSet,
    login_view,
    register_user,
    create_profile,
)

router = routers.DefaultRouter()
router.register(r"profiles", ProfileViewSet)
router.register(r"projects", ProjectViewSet)
router.register(r"certifying-institutions", CertifyingInstitutionViewSet)
router.register(r"certificates", CertificateViewSet)
router.register(r"profile-detail", ProfileViewSet, basename="profile-detail")

urlpatterns = [
    path("api/", include(router.urls)),
    path("", login_view, name="login"),
    path("register/", register_user, name="register"),
    path("create_profile/", create_profile, name="create_profile"),
]
