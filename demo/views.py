from django.views.generic import TemplateView
from utils.constants import Templates


class DemoIndex(TemplateView):
    """Demo Index View"""

    template_name = Templates.DEMO.value


demo_index = DemoIndex.as_view()
