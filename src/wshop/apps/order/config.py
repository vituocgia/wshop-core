from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class OrderConfig(AppConfig):
    label = 'order'
    name = 'wshop.apps.order'
    verbose_name = _('Order')
