from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls
from rest_framework.routers import DefaultRouter
from polls_api.views import PollViewSet

router = DefaultRouter()
router.register("polls", PollViewSet, basename="polls")

app_name = "polls_api"
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
] + debug_toolbar_urls()
