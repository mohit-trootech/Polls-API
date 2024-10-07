from django import forms
from utils.constants import THEME_CHOICES, SELECT_CLASS


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
