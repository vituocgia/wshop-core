from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CheckoutConfig(AppConfig):
    label = 'checkout'
    name = 'wshop.apps.checkout'
    verbose_name = _('Checkout')
