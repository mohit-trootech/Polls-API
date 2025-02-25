from django import forms
from utils.constants import THEME_CHOICES, SELECT_CLASS, FORM_CLASS, FORM_LABELS
from django.contrib.auth.models import User


class Themes(forms.Form):
    theme = forms.ChoiceField(
        choices=THEME_CHOICES,
        widget=forms.Select(
            attrs={
                "class": SELECT_CLASS,
                "id": "themeSelect",
                "required": False,
            }
        ),
    )


class NewsLetter(forms.Form):
    subscribe = forms.EmailField(
        widget=forms.TextInput(attrs={"class": "grow", "type": "email"})
    )


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
        ]
        widgets = {}
        labels = {}
        input_option = forms.TextInput

        for field in fields:
            if field == "email":
                input_option = forms.EmailInput
            widgets[field] = input_option(attrs={"class": FORM_CLASS})
            labels[field] = FORM_LABELS.get(field)
