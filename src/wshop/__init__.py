import os

# Use 'dev', 'beta', or 'final' as the 4th element to indicate release type.
VERSION = (1, 6, 0, 'rc2')


def get_short_version():
    return '%s.%s' % (VERSION[0], VERSION[1])


def get_version():
    version = '%s.%s' % (VERSION[0], VERSION[1])
    # Append 3rd digit if > 0
    if VERSION[2]:
        version = '%s.%s' % (version, VERSION[2])
    elif VERSION[3] != 'final':
        version = '%s %s' % (version, VERSION[3])
        if len(VERSION) == 5:
            version = '%s %s' % (version, VERSION[4])
    return version


# Cheeky setting that allows each template to be accessible by two paths.
# Eg: the template 'wshop/templates/wshop/base.html' can be accessed via both
# 'base.html' and 'wshop/base.html'.  This allows Wshop's templates to be
# extended by templates with the same filename
WSHOP_MAIN_TEMPLATE_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'templates/wshop')

WSHOP_CORE_APPS = [
    'wshop',
    'wshop.apps.analytics',
    'wshop.apps.checkout',
    'wshop.apps.address',
    'wshop.apps.shipping',
    'wshop.apps.catalogue',
    'wshop.apps.catalogue.reviews',
    'wshop.apps.partner',
    'wshop.apps.basket',
    'wshop.apps.payment',
    'wshop.apps.offer',
    'wshop.apps.order',
    'wshop.apps.customer',
    'wshop.apps.promotions',
    'wshop.apps.search',
    'wshop.apps.voucher',
    'wshop.apps.wishlists',
    'wshop.apps.dashboard',
    'wshop.apps.dashboard.reports',
    'wshop.apps.dashboard.users',
    'wshop.apps.dashboard.orders',
    'wshop.apps.dashboard.promotions',
    'wshop.apps.dashboard.catalogue',
    'wshop.apps.dashboard.offers',
    'wshop.apps.dashboard.partners',
    'wshop.apps.dashboard.pages',
    'wshop.apps.dashboard.ranges',
    'wshop.apps.dashboard.reviews',
    'wshop.apps.dashboard.vouchers',
    'wshop.apps.dashboard.communications',
    'wshop.apps.dashboard.shipping',
    # 3rd-party apps that wshop depends on
    'haystack',
    'treebeard',
    'sorl.thumbnail',
    'django_tables2',
]


def get_core_apps(overrides=None):
    """
    Return a list of wshop's apps amended with any passed overrides
    """
    if not overrides:
        return WSHOP_CORE_APPS

    # Conservative import to ensure that this file can be loaded
    # without the presence Django.
    from django.utils import six
    if isinstance(overrides, six.string_types):
        raise ValueError(
            "get_core_apps expects a list or tuple of apps "
            "to override")

    def get_app_label(app_label, overrides):
        pattern = app_label.replace('wshop.apps.', '')
        for override in overrides:
            if override.endswith(pattern):
                if 'dashboard' in override and 'dashboard' not in pattern:
                    continue
                return override
        return app_label

    apps = []
    for app_label in WSHOP_CORE_APPS:
        apps.append(get_app_label(app_label, overrides))
    return apps
