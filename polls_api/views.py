from typing import Any
from rest_framework import permissions, viewsets
from polls_api.serializers import PollSerializer
from polls_api.models import Poll, User
from utils.utils import StandardPagination, get_repository_star, get_api_stats
from django.views.generic import TemplateView
from utils.constants import Templates


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [permissions.IsAuthenticated]
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
