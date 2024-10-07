from rest_framework import permissions, viewsets
from polls_api.serializers import PollSerializer
from polls_api.models import Poll, User
from utils.utils import StandardPagination
from django.views.generic import TemplateView
from utils.constants import Templates


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardPagination


class IndexView(TemplateView):
    template_name = Templates.INDEX.value


index_view = IndexView.as_view()


class AboutView(TemplateView):
    template_name = Templates.ABOUT.value


about_view = AboutView.as_view()
