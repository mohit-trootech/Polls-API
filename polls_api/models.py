from django.db import models
from django_extensions.db.models import TimeStampedModel, TitleSlugDescriptionModel
from django_markdown_model.fields import MarkDownField
from django.contrib.auth.models import AbstractUser
from uuid import uuid4
from utils.constants import ModelConstants


class User(AbstractUser):
    """abstract user model"""

    api = models.UUIDField(default=uuid4, editable=False)

    def __str__(self):
        """model representation"""
        return self.username


class Poll(TimeStampedModel, TitleSlugDescriptionModel):
    """base polls question model"""

    image = models.URLField(null=True, blank=True)
    description = MarkDownField(blank=True, null=True)
    user = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name=ModelConstants.USERS.value
    )

    def __str__(self):
        """model representation"""
        return self.title

    class Meta:
        ordering = ["?"]


class Choice(models.Model):
    """choice model for poll"""

    poll = models.ForeignKey(
        "Poll", on_delete=models.CASCADE, related_name=ModelConstants.CHOICES.value
    )
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """model representation"""
        return self.choice_text


class ApiStats(models.Model):
    hit = models.IntegerField(default=0)
