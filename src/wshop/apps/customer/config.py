from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CustomerConfig(AppConfig):
    label = 'customer'
    name = 'wshop.apps.customer'
    verbose_name = _('Customer')

    def ready(self):
        from . import receivers  # noqa
        from .alerts import receivers  # noqa
