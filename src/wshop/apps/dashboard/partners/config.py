from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class PartnersDashboardConfig(AppConfig):
    label = 'partners_dashboard'
    name = 'wshop.apps.dashboard.partners'
    verbose_name = _('Partners dashboard')
