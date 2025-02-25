from django.urls import path
from utils.constants import Urls
from demo.views import demo_index


urlpatterns = [path("", demo_index, name=Urls.DEMO.value)]
