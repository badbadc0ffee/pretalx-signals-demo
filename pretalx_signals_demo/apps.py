from django.apps import AppConfig
from django.utils.translation import gettext_lazy

from . import __version__


class PluginApp(AppConfig):
    name = "pretalx_signals_demo"
    verbose_name = "pretalx signals demo"

    class PretalxPluginMeta:
        name = gettext_lazy("pretalx signals demo")
        author = "Florian Mösch"
        description = gettext_lazy("pretalx plugin to test all html signals")
        visible = True
        version = __version__
        category = "INTEGRATION"

    def ready(self):
        from . import signals  # NOQA
