from django.contrib.auth import login
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from super_portfolio import settings
from .forms import UserForm
from django.shortcuts import redirect, render
from .serializers import UserLoginSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework import viewsets, status
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
        # if not request.user.is_authenticated:
        #     return Response(status.HTTP_403_FORBIDDEN)
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
            print("register", user)
            return redirect("login")
    return render(request, "register.html", context={"user_form": user_form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        print("user", form)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("profile-detail", pk=user.id)
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"login_form": form})


class LoginAPIView(APIView):
    permission_classes = []
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            user_id = new_data["id"]
            return HttpResponseRedirect(
                reverse("profile-detail", args=[user_id])
            )
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
