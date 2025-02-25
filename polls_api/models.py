from django.db import models
from django_extensions.db.models import TimeStampedModel, TitleSlugDescriptionModel
from django_markdown_model.fields import MarkDownField
from utils.constants import ModelConstants


class Poll(TimeStampedModel, TitleSlugDescriptionModel):
    """base polls question model"""

    image = models.URLField(null=True, blank=True)
    description = MarkDownField(blank=True, null=True)
    user = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name=ModelConstants.USERS.value
    )

    @property
    def get_total_votes(self):
        """get total votes"""
        return sum([vote.votes for vote in self.choices.all()])

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
    title = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """model representation"""
        return self.title


class ApiStats(models.Model):
    hit = models.IntegerField(default=0)
