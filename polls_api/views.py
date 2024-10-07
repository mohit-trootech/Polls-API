from rest_framework import permissions, viewsets
from polls_api.serializers import PollSerializer, ChoiceSerializer
from polls_api.models import Poll, User


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [permissions.IsAuthenticated]
