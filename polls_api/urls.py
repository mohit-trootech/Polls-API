from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls
from rest_framework.routers import DefaultRouter, SimpleRouter
from polls_api.views import (
    PollViewSet,
    index_view,
    about_view,
    ChoiceViewSet,
    LoginView,
    RegisterView,
    LogoutView,
    ProfileView,
)
from utils.constants import Urls
from rest_framework_nested import routers

""
router = DefaultRouter()
router.register("polls", PollViewSet)
router.register("choices", ChoiceViewSet)
app_name = "polls_api"
urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/register/", RegisterView.as_view(), name="signup"),
    path("accounts/login/", LoginView.as_view(), name="login"),
    path("accounts/logout/", LogoutView.as_view(), name="logout"),
    path("accounts/profile/", ProfileView.as_view(), name="profile"),
    path("api/", include(router.urls)),
    path("", index_view, name=Urls.INDEX.value),
    path("about/", about_view, name=Urls.ABOUT.value),
    path("demo/", include("demo.urls")),
] + debug_toolbar_urls()
