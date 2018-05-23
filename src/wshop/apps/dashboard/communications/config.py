from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CommunicationsDashboardConfig(AppConfig):
    label = 'communications_dashboard'
    name = 'wshop.apps.dashboard.communications'
    verbose_name = _('Communications dashboard')
