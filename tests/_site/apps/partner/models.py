from django.db import models

from wshop.apps.partner import abstract_models


class StockRecord(abstract_models.AbstractStockRecord):
    # Dummy additional field
    offer_name = models.CharField(max_length=128, null=True, blank=True)


from wshop.apps.partner.models import *  # noqa
