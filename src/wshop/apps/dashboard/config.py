from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class DashboardConfig(AppConfig):
    label = 'dashboard'
    name = 'wshop.apps.dashboard'
    verbose_name = _('Dashboard')
