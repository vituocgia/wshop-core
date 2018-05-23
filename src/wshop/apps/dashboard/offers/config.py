from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class OffersDashboardConfig(AppConfig):
    label = 'offers_dashboard'
    name = 'wshop.apps.dashboard.offers'
    verbose_name = _('Offers dashboard')
