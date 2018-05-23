from collections import OrderedDict

from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _

WSHOP_SHOP_NAME = 'Wshop'
WSHOP_SHOP_TAGLINE = ''
WSHOP_HOMEPAGE = reverse_lazy('promotions:home')

# Dynamic class loading
WSHOP_DYNAMIC_CLASS_LOADER = 'wshop.core.loading.default_class_loader'

# Basket settings
WSHOP_BASKET_COOKIE_LIFETIME = 7 * 24 * 60 * 60
WSHOP_BASKET_COOKIE_OPEN = 'wshop_open_basket'
WSHOP_BASKET_COOKIE_SECURE = False
WSHOP_MAX_BASKET_QUANTITY_THRESHOLD = 10000

# Recently-viewed products
WSHOP_RECENTLY_VIEWED_COOKIE_LIFETIME = 7 * 24 * 60 * 60
WSHOP_RECENTLY_VIEWED_COOKIE_NAME = 'wshop_history'
WSHOP_RECENTLY_VIEWED_COOKIE_SECURE = False
WSHOP_RECENTLY_VIEWED_PRODUCTS = 20

# Currency
WSHOP_DEFAULT_CURRENCY = 'GBP'

# Paths
WSHOP_IMAGE_FOLDER = 'images/products/%Y/%m/'
WSHOP_PROMOTION_FOLDER = 'images/promotions/'
WSHOP_DELETE_IMAGE_FILES = True

# Copy this image from wshop/static/img to your MEDIA_ROOT folder.
# It needs to be there so Sorl can resize it.
WSHOP_MISSING_IMAGE_URL = 'image_not_found.jpg'
WSHOP_UPLOAD_ROOT = '/tmp'

# Address settings
WSHOP_REQUIRED_ADDRESS_FIELDS = ('first_name', 'last_name', 'line1',
                                 'line4', 'postcode', 'country')

# Pagination settings

WSHOP_OFFERS_PER_PAGE = 20
WSHOP_PRODUCTS_PER_PAGE = 20
WSHOP_REVIEWS_PER_PAGE = 20
WSHOP_NOTIFICATIONS_PER_PAGE = 20
WSHOP_EMAILS_PER_PAGE = 20
WSHOP_ORDERS_PER_PAGE = 20
WSHOP_ADDRESSES_PER_PAGE = 20
WSHOP_STOCK_ALERTS_PER_PAGE = 20
WSHOP_DASHBOARD_ITEMS_PER_PAGE = 20

# Checkout
WSHOP_ALLOW_ANON_CHECKOUT = False

# Promotions
WSHOP_PROMOTION_POSITIONS = (('page', 'Page'),
                             ('right', 'Right-hand sidebar'),
                             ('left', 'Left-hand sidebar'))

# Reviews
WSHOP_ALLOW_ANON_REVIEWS = True
WSHOP_MODERATE_REVIEWS = False

# Accounts
WSHOP_ACCOUNTS_REDIRECT_URL = 'customer:profile-view'

# This enables sending alert notifications/emails instantly when products get
# back in stock by listening to stock record update signals.
# This might impact performance for large numbers of stock record updates.
# Alternatively, the management command ``wshop_send_alerts`` can be used to
# run periodically, e.g. as a cron job. In this case eager alerts should be
# disabled.
WSHOP_EAGER_ALERTS = True

# Registration
WSHOP_SEND_REGISTRATION_EMAIL = True
WSHOP_FROM_EMAIL = 'wshop@example.com'

# Slug handling
WSHOP_SLUG_FUNCTION = 'wshop.core.utils.default_slugifier'
WSHOP_SLUG_MAP = {}
WSHOP_SLUG_BLACKLIST = []
WSHOP_SLUG_ALLOW_UNICODE = False

# Cookies
WSHOP_COOKIES_DELETE_ON_LOGOUT = ['wshop_recently_viewed_products', ]

# Hidden Wshop features, e.g. wishlists or reviews
WSHOP_HIDDEN_FEATURES = []

# Menu structure of the dashboard navigation
WSHOP_DASHBOARD_NAVIGATION = [
    {
        'label': _('Dashboard'),
        'icon': 'icon-th-list',
        'url_name': 'dashboard:index',
    },
    {
        'label': _('Catalogue'),
        'icon': 'icon-sitemap',
        'children': [
            {
                'label': _('Products'),
                'url_name': 'dashboard:catalogue-product-list',
            },
            {
                'label': _('Product Types'),
                'url_name': 'dashboard:catalogue-class-list',
            },
            {
                'label': _('Categories'),
                'url_name': 'dashboard:catalogue-category-list',
            },
            {
                'label': _('Ranges'),
                'url_name': 'dashboard:range-list',
            },
            {
                'label': _('Low stock alerts'),
                'url_name': 'dashboard:stock-alert-list',
            },
        ]
    },
    {
        'label': _('Fulfilment'),
        'icon': 'icon-shopping-cart',
        'children': [
            {
                'label': _('Orders'),
                'url_name': 'dashboard:order-list',
            },
            {
                'label': _('Statistics'),
                'url_name': 'dashboard:order-stats',
            },
            {
                'label': _('Partners'),
                'url_name': 'dashboard:partner-list',
            },
            # The shipping method dashboard is disabled by default as it might
            # be confusing. Weight-based shipping methods aren't hooked into
            # the shipping repository by default (as it would make
            # customising the repository slightly more difficult).
            # {
            #     'label': _('Shipping charges'),
            #     'url_name': 'dashboard:shipping-method-list',
            # },
        ]
    },
    {
        'label': _('Customers'),
        'icon': 'icon-group',
        'children': [
            {
                'label': _('Customers'),
                'url_name': 'dashboard:users-index',
            },
            {
                'label': _('Stock alert requests'),
                'url_name': 'dashboard:user-alert-list',
            },
        ]
    },
    {
        'label': _('Offers'),
        'icon': 'icon-bullhorn',
        'children': [
            {
                'label': _('Offers'),
                'url_name': 'dashboard:offer-list',
            },
            {
                'label': _('Vouchers'),
                'url_name': 'dashboard:voucher-list',
            },
            {
                'label': _('Voucher Sets'),
                'url_name': 'dashboard:voucher-set-list',
            },

        ],
    },
    {
        'label': _('Content'),
        'icon': 'icon-folder-close',
        'children': [
            {
                'label': _('Content blocks'),
                'url_name': 'dashboard:promotion-list',
            },
            {
                'label': _('Content blocks by page'),
                'url_name': 'dashboard:promotion-list-by-page',
            },
            {
                'label': _('Pages'),
                'url_name': 'dashboard:page-list',
            },
            {
                'label': _('Email templates'),
                'url_name': 'dashboard:comms-list',
            },
            {
                'label': _('Reviews'),
                'url_name': 'dashboard:reviews-list',
            },
        ]
    },
    {
        'label': _('Reports'),
        'icon': 'icon-bar-chart',
        'url_name': 'dashboard:reports-index',
    },
]
WSHOP_DASHBOARD_DEFAULT_ACCESS_FUNCTION = 'wshop.apps.dashboard.nav.default_access_fn'  # noqa

# Search facets
WSHOP_SEARCH_FACETS = {
    'fields': OrderedDict([
        # The key for these dicts will be used when passing facet data
        # to the template. Same for the 'queries' dict below.
        ('product_class', {'name': _('Type'), 'field': 'product_class'}),
        ('rating', {'name': _('Rating'), 'field': 'rating'}),
        # You can specify an 'options' element that will be passed to the
        # SearchQuerySet.facet() call.
        # For instance, with Elasticsearch backend, 'options': {'order': 'term'}
        # will sort items in a facet by title instead of number of items.
        # It's hard to get 'missing' to work
        # correctly though as of Solr's hilarious syntax for selecting
        # items without a specific facet:
        # http://wiki.apache.org/solr/SimpleFacetParameters#facet.method
        # 'options': {'missing': 'true'}
    ]),
    'queries': OrderedDict([
        ('price_range',
         {
             'name': _('Price range'),
             'field': 'price',
             'queries': [
                 # This is a list of (name, query) tuples where the name will
                 # be displayed on the front-end.
                 (_('0 to 20'), u'[0 TO 20]'),
                 (_('20 to 40'), u'[20 TO 40]'),
                 (_('40 to 60'), u'[40 TO 60]'),
                 (_('60+'), u'[60 TO *]'),
             ]
         }),
    ]),
}


WSHOP_PROMOTIONS_ENABLED = True
WSHOP_PRODUCT_SEARCH_HANDLER = None
