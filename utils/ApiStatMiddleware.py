from polls_api.models import ApiStats
from django.db.models import F


class ApiStatMiddleware:

    PATH = "/api/"

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if self.PATH in request.path:
            stats = ApiStats.objects.first()
            stats.hit = F("hit") + 1
            stats.save(update_fields=["hit"])
        response = self.get_response(request)

        return response
