from rest_framework import routers
from .views import ProfileViewSet
from django.urls import path, include
from .views import (
    ProfileViewSet,
    ProjectViewSet,
    CertifyingInstitutionViewSet,
    CertificateViewSet,
    LoginAPIView,
    login_view,
    register_user,
)

router = routers.DefaultRouter()
# router.register(r"user", LoginAPIView)
router.register(r"profiles", ProfileViewSet)
router.register(r"projects", ProjectViewSet)
router.register(r"certifying-institutions", CertifyingInstitutionViewSet)
router.register(r"certificates", CertificateViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path(
        "profile-details/<int:pk>/",
        ProfileViewSet.as_view({"get": "retrieve"}),
        name="profile-details",
    ),
    path("", login_view, name="login"),
    path("register/", register_user, name="register"),
    path("api-login/", LoginAPIView.as_view(), name="api-login"),
]
