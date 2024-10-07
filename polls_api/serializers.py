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
        fields = [
            "id",
            "choices",
            "created",
            "modified",
            "title",
            "description",
            "slug",
            "image",
            "user",
        ]
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

    @staticmethod
    def update_choices_data(choices):
        if isinstance(choices, str):
            from ast import literal_eval

            choices = literal_eval(choices)
        for choice in choices:
            instance = Choice.objects.get(id=choice.get("id"))
            if choice.get("choice_text"):
                instance.choice_text = choice.get("choice_text")
            if choice.get("votes"):
                instance.votes = choice.get("votes")
            instance.save()

    @staticmethod
    def add_vote(id):
        """add vote to vote choice"""
        from django.db.models import F

        choice = Choice.objects.get(id=id)
        choice.votes = F("votes") + 1
        choice.save(update_fields=["votes"])

    def update(self, instance, validated_data):
        request = self.context["request"]
        if request.query_params.get("vote"):
            self.add_vote(request.query_params.get("vote"))
            return instance
        instance = super().update(instance, validated_data)
        if self.initial_data.get("choices"):
            self.update_choices_data(self.initial_data.get("choices"))
        return instance

    def create(self, validated_data):
        poll = Poll(**validated_data)
        poll.save()
        if self.initial_data.get("choices"):
            self.handle_choices_initital_data(self.initial_data.get("choices"), poll)
        return poll
