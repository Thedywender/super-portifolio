from rest_framework import routers
from .views import ProfileViewSet
from django.urls import path, include
from .views import (
    ProfileViewSet,
    ProjectViewSet,
    CertifyingInstitutionViewSet,
    CertificateViewSet,
    login_page,
)

router = routers.DefaultRouter()
router.register(r"profiles", ProfileViewSet)
router.register(r"projects", ProjectViewSet)
router.register(r"certifying-institutions", CertifyingInstitutionViewSet)
router.register(r"certificates", CertificateViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "profile-details/<int:pk>/",
        ProfileViewSet.as_view({"get": "retrieve"}),
        name="profile-details",
    ),
    path("login", login_page, name="login"),
]
