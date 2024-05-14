from rest_framework import viewsets
from .models import Profile, Project, CertifyingInstitution, Certificate
from .serializers import (
    ProfileSerializer,
    ProjectSerializer,
    CertifyingInstitutionSerializer,
    CertificateSerializer,
)
from django.shortcuts import redirect, render
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from .forms import UserForm


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def retrieve(self, request, *args, **kwargs):
        if request.method == "GET":
            profile = Profile.objects.get(id=kwargs["pk"])

            return render(
                request,
                "profile_detail.html",
                {
                    "profile": profile,
                    "certificates": profile.certificates.all(),
                    "projects": profile.projects.all(),
                },
            )
        return super().retrieve(request, *args, **kwargs)


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = [IsAuthenticated]


class CertifyingInstitutionViewSet(viewsets.ModelViewSet):
    serializer_class = CertifyingInstitutionSerializer
    queryset = CertifyingInstitution.objects.all()
    permission_classes = [IsAuthenticated]


class CertificateViewSet(viewsets.ModelViewSet):
    serializer_class = CertificateSerializer
    queryset = Certificate.objects.all()
    permission_classes = [IsAuthenticated]


def login_page(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            profile = Profile(user=user)
            profile.save()
            request.session["user_id"] = user.id
            return redirect("profile-details", pk=profile.id)
    elif request.method == "GET":
        return render(request, "login.html", context={"user_form": UserForm()})
