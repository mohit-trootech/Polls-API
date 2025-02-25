# Utility Polls API
from rest_framework import pagination


class StandardPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


def get_repository_star():
    """
    get github repository star count
    """
    from requests import get

    response = get("https://api.github.com/repos/mohit-trootech/Polls-API").json()
    return response.get("stargazers_count")


def get_api_stats():
    """
    get api stats information
    """
    from polls_api.models import ApiStats

    try:
        hit = ApiStats.objects.first().hit
    except AttributeError:
        ApiStats.objects.create()
        hit = ApiStats.objects.first().hit
    return hit
