from polls_api.models import Poll, Choice
from rest_framework import serializers


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = "__all__"


class PollSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Poll
        read_only_fields = ["id", "slug", "created", "modified", "choices"]
        fields = "__all__"
        depth = True

    @staticmethod
    def handle_choices_initital_data(choices, poll):
        """handle choices by creating creates for poll instance"""
        if isinstance(choices, str):
            from ast import literal_eval

            choices = literal_eval(choices)
        choices_data = []
        limit = 0
        for choice in choices:
            if limit < 4:
                limit += 1
                choices_data.append(Choice(poll=poll, choice_text=choice))
            else:
                break
        Choice.objects.bulk_create(choices_data)

    def create(self, validated_data):
        poll = Poll(**validated_data)
        poll.save()
        if self.initial_data.get("choices"):
            self.handle_choices_initital_data(self.initial_data.get("choices"), poll)
        return poll
