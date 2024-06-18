from django.contrib.auth import login, authenticate, logout
from django.http import Http404

# from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import (
    ProjectForm,
    UserForm,
    ProfileForm,
    CertifyingInstitutionForm,
)
from django.shortcuts import get_object_or_404, redirect, render


from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from rest_framework import viewsets
from .models import (
    Profile,
    Project,
    CertifyingInstitution,
    Certificate,
)
from .serializers import (
    ProfileSerializer,
    ProjectSerializer,
    CertifyingInstitutionSerializer,
    CertificateSerializer,
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)

from django.contrib.auth.forms import AuthenticationForm


@method_decorator(login_required(login_url="login"), name="dispatch")
class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def retrieve(self, request, *args, **kwargs):
        print(request.user, "user")
        if request.method == "GET":
            pk = kwargs.get("pk")
            try:
                profile = Profile.objects.get(pk=pk)
            except Profile.DoesNotExist:
                raise Http404("Profile does not exist")

            return render(
                request,
                "profile_detail.html",
                {
                    "profile": profile,
                    "user_data": request.user,
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


def register_user(request):
    user_form = (
        UserForm(request.POST) if request.method == "POST" else UserForm()
    )
    if request.method == "POST":
        if user_form.is_valid():
            user = user_form.save()
            authenticated_user = authenticate(
                username=user.username, password=request.POST["password1"]
            )
            login(request, authenticated_user)
            return redirect("create_profile")
    return render(
        request, "register_user.html", context={"user_form": user_form}
    )


@login_required(login_url="login")
def create_profile(request):
    profile_form = ProfileForm(request.POST or None)
    if request.method == "POST" and profile_form.is_valid():
        if hasattr(request.user, "profile"):
            return redirect("create_profile")
        profile = profile_form.save(commit=False)
        profile.user = request.user
        profile.save()
        return redirect("login")
    return render(
        request, "create_profile.html", context={"profile_form": profile_form}
    )


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        print("user", form)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            profile = Profile.objects.get(user=user)
            return redirect("profile-detail", pk=profile.id)
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"login_form": form})


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required(login_url="login")
def create_project(request):
    project_form = ProjectForm(request.POST or None)
    if request.method == "POST" and project_form.is_valid():
        project = project_form.save(commit=False)
        project.profile = request.user.profile
        project.save()
        return redirect("profile-detail", pk=request.user.profile.id)
    return render(
        request, "create_project.html", {"project_form": project_form}
    )


@login_required(login_url="login")
def update_project(request, project_id):
    project = get_object_or_404(
        Project, pk=project_id, profile=request.user.profile
    )
    if request.method == "POST":
        project_form = ProjectForm(request.POST, instance=project)
        if project_form.is_valid():
            project_form.save()
            return redirect("profile-detail", pk=request.user.profile.id)
    else:
        project_form = ProjectForm(instance=project)

    return render(
        request,
        "update_project.html",
        {"project_form": project_form, "project": project},
    )


@login_required(login_url="login")
def delete_project(request, project_id):
    if request.method == "POST":
        project = get_object_or_404(
            Project, id=project_id, profile=request.user.profile
        )
        project.delete()
        return redirect("profile-detail", pk=request.user.profile.id)
    else:
        return redirect("profile-detail", pk=request.user.profile.id)


def create_institution(request):
    institution_form = CertifyingInstitutionForm(request.POST or None)
    if request.method == "POST" and institution_form.is_valid():
        institution_form.save()
        return redirect("profile-detail")
    return render(
        request,
        "create_institution.html",
        {"institution_form": institution_form},
    )


# OBS: esta criando a instituição mas não consegue retornar ao profile_details porque falta a ralação do id
# não esquecer e criar
