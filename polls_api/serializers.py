from polls_api.models import Poll, Choice
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    def validate_first_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Data must be in alphabets.")
        return value

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "is_active",
            "last_login",
            "date_joined",
        ]


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ["id", "title", "votes"]


class DynamicModelSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        fields = self.context["request"].query_params.get("fields")
        if fields is not None:
            allowed = set(fields.values())
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class PollSerializer(DynamicModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Poll
        read_only_fields = [
            "id",
            "slug",
            "created",
            "get_total_votes",
            "modified",
            "choices",
        ]
        fields = [
            "id",
            "choices",
            "created",
            "modified",
            "title",
            "description",
            "slug",
            "image",
            "get_total_votes",
            "user",
        ]
        depth = True

    def create(self, validated_data):
        instance = super().create(validated_data)
        choices = self.initial_data.get("choices")
        if choices:
            choices = eval(choices) if isinstance(choices, str) else choices
            for choice in choices:
                serializer = ChoiceSerializer(
                    data={"title": choice, "poll": instance.id}
                )
                serializer.is_valid(raise_exception=True)
                serializer.save()
        return instance

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        if "vote" in self.context["request"].query_params:

            vote = self.context["request"].query_params["vote"]
            vote = eval(vote) if isinstance(vote, str) else vote
            try:
                choice = Choice.objects.get(id=vote)
                serializer = ChoiceSerializer(
                    choice, data={"votes": choice.votes + 1}, partial=True
                )
                serializer.is_valid(raise_exception=True)
                serializer.save()
            except Choice.DoesNotExist:
                from rest_framework.exceptions import NotFound

                raise NotFound("Choice Not Found")
        return instance
