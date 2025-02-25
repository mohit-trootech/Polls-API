from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.http.response import HttpResponse as HttpResponse
from rest_framework import permissions, viewsets, renderers, views, response, status
from django.shortcuts import redirect
from django.urls import reverse
from polls_api.serializers import (
    PollSerializer,
    ChoiceSerializer,
    UserSerializer,
    LoginSerializer,
)
from polls_api.models import Poll, Choice
from utils.utils import StandardPagination, get_repository_star, get_api_stats
from django.views.generic import TemplateView, UpdateView, RedirectView
from utils.constants import Templates
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, JsonResponse
from polls_api.forms import UserUpdateForm
from django.contrib.auth.models import User


class ProfileView(UpdateView):
    template_name = "polls_api/profile.html"
    context_object_name = "user"
    form_class = UserUpdateForm
    success_url = "/accounts/profile/"

    def get_object(self, *args, **kwargs):
        return User.objects.get(username=self.request.user)


class RegisterView(views.APIView):
    serializer_class = UserSerializer
    renderer_classes = [renderers.TemplateHTMLRenderer]
    template_name = "polls_api/register.html"
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        return response.Response(status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            save_user = user_serializer.save()
            save_user.set_password(save_user.password)
            save_user.is_active = True
            save_user.save()
            return JsonResponse(
                {"message": "User Registered Successfully."}, status=status.HTTP_200_OK
            )
        else:
            return JsonResponse(
                {"message": "User with username Already Exists"},
                status=status.HTTP_409_CONFLICT,
            )


class LoginView(views.APIView):
    renderer_classes = [renderers.TemplateHTMLRenderer]
    template_name = "polls_api/login.html"
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        return response.Response(status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        login_serializer = LoginSerializer(data=request.data)
        login_serializer.is_valid()
        user = authenticate(request=request, **login_serializer.validated_data)
        if user:
            login(request, user)
            return JsonResponse(
                {"message": "User Logged in Successfully."},
                status=status.HTTP_200_OK,
            )
        else:
            return JsonResponse(
                {"message": "User Not Found!"},
                status=status.HTTP_404_NOT_FOUND,
            )


class LogoutView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        logout(request)
        return redirect(reverse("login"))


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    pagination_class = StandardPagination

    def get_queryset(self):
        from django.db.models import Q

        filter_params = self.request.query_params

        return (
            super()
            .get_queryset()
            .order_by(
                filter_params.get("orderby") if filter_params.get("orderby") else "?"
            )
        )


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class IndexView(TemplateView):
    template_name = Templates.INDEX.value

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["star"] = get_repository_star()
        context["hit"] = get_api_stats()
        context["count"] = User.objects.count()
        return context


index_view = IndexView.as_view()


class AboutView(TemplateView):
    template_name = Templates.ABOUT.value


about_view = AboutView.as_view()
