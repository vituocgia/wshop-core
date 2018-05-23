from wshop.apps.customer.views import AccountSummaryView as WshopAccountSummaryView


class AccountSummaryView(WshopAccountSummaryView):
    # just here to test import in loading_tests:ClassLoadingWithLocalOverrideTests
    pass
