from django.contrib import admin
from polls_api.models import Poll, Choice, User


admin.site.register(Choice)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "is_superuser", "is_active")
    list_filter = ["date_joined", "last_login"]
    ordering = ["id"]
    search_fields = ["username"]
    filter_horizontal = ["groups", "user_permissions"]
    readonly_fields = ["id", "date_joined", "last_login", "password"]
    fieldsets = [
        (
            "User Info",
            {
                "fields": [
                    "id",
                    "first_name",
                    "last_name",
                    "username",
                    "email",
                    "password",
                ]
            },
        ),
        (
            "Status Info",
            {
                "classes": ["collapse"],
                "fields": ["is_staff", "is_superuser", "is_active"],
            },
        ),
        (
            "Login Info",
            {"classes": ["collapse"], "fields": ["date_joined", "last_login"]},
        ),
        (
            "Group Info",
            {"classes": ["collapse"], "fields": ["groups", "user_permissions"]},
        ),
    ]


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
