from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class VoucherConfig(AppConfig):
    label = 'voucher'
    name = 'wshop.apps.voucher'
    verbose_name = _('Voucher')

    def ready(self):
        from . import receivers  # noqa
