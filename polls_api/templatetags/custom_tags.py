from django.template import Library

register = Library()


@register.simple_tag
def format_number(value, *args, **kwargs):
    try:
        value = int(value)
        for unit in ["", "K", "M", "B", "T"]:
            if abs(value) < 1000.0:
                return f"{value:6.2f}{unit}"
            value /= 1000.0
        return f"{value:6.2f}B"
    except TypeError:
        return "Nan"
