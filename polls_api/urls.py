from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls
from rest_framework.routers import DefaultRouter
from polls_api.views import PollViewSet, index_view, about_view
from utils.constants import Urls

router = DefaultRouter()
router.register("polls", PollViewSet, basename="polls")

app_name = "polls_api"
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("", index_view, name=Urls.INDEX.value),
    path("about/", about_view, name=Urls.ABOUT.value),
] + debug_toolbar_urls()
