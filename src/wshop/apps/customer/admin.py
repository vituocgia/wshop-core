from django.contrib import admin

from wshop.core.loading import get_model

CommunicationEventType = get_model('customer', 'CommunicationEventType')
Email = get_model('customer', 'Email')


admin.site.register(Email)
admin.site.register(CommunicationEventType)
