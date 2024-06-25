from rest_framework import routers
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    ProfileViewSet,
    ProjectViewSet,
    CertifyingInstitutionViewSet,
    CertificateViewSet,
    login_view,
    register_user,
    create_profile,
    logout_view,
    create_project,
    update_project,
    delete_project,
    create_institution,
    create_certificate,
    update_certificate,
    delete_certificate,
    update_profile,
)

router = routers.DefaultRouter()
router.register(r"profiles", ProfileViewSet)
router.register(r"projects", ProjectViewSet)
router.register(r"certifying-institutions", CertifyingInstitutionViewSet)
router.register(r"certificates", CertificateViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("", login_view, name="login"),
    path("register/", register_user, name="register"),
    path("create_profile/", create_profile, name="create_profile"),
    path("logout/", logout_view, name="logout"),
    path("create_project/", create_project, name="create_project"),
    path(
        "update_profile/<int:profile_id>/",
        update_profile,
        name="update_profile",
    ),
    path(
        "update_project/<int:project_id>/",
        update_project,
        name="update_project",
    ),
    path(
        "delete_project/<int:project_id>/",
        delete_project,
        name="delete_project",
    ),
    path("create_institution/", create_institution, name="create_institution"),
    path("create_certificate/", create_certificate, name="create_certificate"),
    path(
        "update_certificate/<int:certificate_id>/",
        update_certificate,
        name="update_certificate",
    ),
    path(
        "delete_certificate/<int:certificate_id>/",
        delete_certificate,
        name="delete_certificate",
    ),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
