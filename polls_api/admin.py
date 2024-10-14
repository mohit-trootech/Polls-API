from django.contrib import admin
from polls_api.models import Poll, Choice


admin.site.register(Choice)


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ("id", "title", "created", "modified")
    readonly_fields = ("id", "created", "modified")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "id",
                    "title",
                    "description",
                    "image",
                    "created",
                    "modified",
                    "user",
                ),
            },
        ),
    )
    list_filter = ["created", "modified"]
    ordering = ["-created"]
    search_fields = ["title", "description"]
