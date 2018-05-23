from django.conf import settings
from django.db.models.signals import post_save

from wshop.core.loading import get_model


def send_product_alerts(sender, instance, created, **kwargs):
    if kwargs.get('raw', False):
        return
    from wshop.apps.customer.alerts import utils
    utils.send_product_alerts(instance.product)


if settings.WSHOP_EAGER_ALERTS:
    StockRecord = get_model('partner', 'StockRecord')
    post_save.connect(send_product_alerts, sender=StockRecord)
