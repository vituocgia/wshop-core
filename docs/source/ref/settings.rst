==============
Wshop settings
==============

This is a comprehensive list of all the settings Wshop provides.  All settings
are optional.

Display settings
================

``WSHOP_SHOP_NAME``
-------------------

Default: ``'Wshop'``

The name of your e-commerce shop site.  This is shown as the main logo within
the default templates.

``WSHOP_SHOP_TAGLINE``
----------------------

Default: ``''``

The tagline that is displayed next to the shop name and in the browser title.

``WSHOP_HOMEPAGE``
------------------

Default: ``reverse_lazy('promotions:home')``

URL of home page of your site. This value is used for `Home` link in
navigation and redirection page after logout. Useful if you use a different app
to serve your homepage.

``WSHOP_ACCOUNTS_REDIRECT_URL``
-------------------------------

Default: ``'customer:profile-view'``

Wshop has a view that gets called any time the user clicks on 'My account' or
similar. By default it's a dumb redirect to the view configured with this
setting. But you could also override the view to display a more useful
account summary page or such like.

``WSHOP_RECENTLY_VIEWED_PRODUCTS``
----------------------------------

Default: 20

The number of recently viewed products to store.

``WSHOP_RECENTLY_VIEWED_COOKIE_LIFETIME``
-----------------------------------------

Default: 604800 (1 week in seconds)

The time to live for the cookie in seconds.

``WSHOP_RECENTLY_VIEWED_COOKIE_NAME``
-------------------------------------

Default: ``'wshop_history'``

The name of the cookie for showing recently viewed products.

``WSHOP_HIDDEN_FEATURES``
-------------------------

Defaults: ``[]``

Allows to disable particular Wshop feature in application and templates.
More information in the :doc:`/howto/how_to_disable_an_app_or_feature` document.

Pagination
----------

There are a number of settings that control pagination in Wshop's views. They
all default to 20.

- ``WSHOP_PRODUCTS_PER_PAGE``
- ``WSHOP_OFFERS_PER_PAGE``
- ``WSHOP_REVIEWS_PER_PAGE``
- ``WSHOP_NOTIFICATIONS_PER_PAGE``
- ``WSHOP_EMAILS_PER_PAGE``
- ``WSHOP_ORDERS_PER_PAGE``
- ``WSHOP_ADDRESSES_PER_PAGE``
- ``WSHOP_STOCK_ALERTS_PER_PAGE``
- ``WSHOP_DASHBOARD_ITEMS_PER_PAGE``

.. _wshop_search_facets:

``WSHOP_SEARCH_FACETS``
-----------------------

A dictionary that specifies the facets to use with the search backend.  It
needs to be a dict with keys ``fields`` and ``queries`` for field- and
query-type facets. Field-type facets can get an 'options' element with parameters like facet
sorting, filtering, etc.
The default is::

    WSHOP_SEARCH_FACETS = {
        'fields': OrderedDict([
            ('product_class', {'name': _('Type'), 'field': 'product_class'}),
            ('rating', {'name': _('Rating'), 'field': 'rating'}),
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

``WSHOP_PRODUCT_SEARCH_HANDLER``
--------------------------------

The search handler to be used in the product list views. If ``None``,
Wshop tries to guess the correct handler based on your Haystack settings.

Default::

    None

``WSHOP_PROMOTION_POSITIONS``
-----------------------------

Default::

    WSHOP_PROMOTION_POSITIONS = (('page', 'Page'),
                                 ('right', 'Right-hand sidebar'),
                                 ('left', 'Left-hand sidebar'))

The choice of display locations available when editing a promotion. Only
useful when using a new set of templates.

.. _WSHOP_DASHBOARD_NAVIGATION:

``WSHOP_DASHBOARD_NAVIGATION``
------------------------------

Default: see ``wshop.defaults`` (too long to include here).

A list of dashboard navigation elements. Usage is explained in
:doc:`/howto/how_to_configure_the_dashboard_navigation`.

``WSHOP_DASHBOARD_DEFAULT_ACCESS_FUNCTION``
-------------------------------------------

Default: ``'wshop.apps.dashboard.nav.default_access_fn'``

``WSHOP_DASHBOARD_NAVIGATION`` allows passing an access function for each node
which is used to determine whether to show the node for a specific user or not.
If no access function is defined, the function specified here is used.
The default function integrates with the permission-based dashboard and shows
the node if the user will be able to access it. That should be sufficient for
most cases.

Order settings
==============

``WSHOP_INITIAL_ORDER_STATUS``
------------------------------

The initial status used when a new order is submitted. This has to be a status
that is defined in the ``WSHOP_ORDER_STATUS_PIPELINE``.

``WSHOP_INITIAL_LINE_STATUS``
-----------------------------

The status assigned to a line item when it is created as part of an new order. It
has to be a status defined in ``WSHOP_LINE_STATUS_PIPELINE``.

``WSHOP_ORDER_STATUS_PIPELINE``
-------------------------------

Default: ``{}``

The pipeline defines the statuses that an order or line item can have and what
transitions are allowed in any given status. The pipeline is defined as a
dictionary where the keys are the available statuses. Allowed transitions are
defined as iterable values for the corresponding status.

A sample pipeline (as used in the Wshop sandbox) might look like this::

    WSHOP_INITIAL_ORDER_STATUS = 'Pending'
    WSHOP_INITIAL_LINE_STATUS = 'Pending'
    WSHOP_ORDER_STATUS_PIPELINE = {
        'Pending': ('Being processed', 'Cancelled',),
        'Being processed': ('Processed', 'Cancelled',),
        'Cancelled': (),
    }

``WSHOP_ORDER_STATUS_CASCADE``
------------------------------

This defines a mapping of status changes for order lines which 'cascade' down
from an order status change.

For example::

    WSHOP_ORDER_STATUS_CASCADE = {
        'Being processed': 'In progress'
    }

With this mapping, when an order has it's status set to 'Being processed', all
lines within it have their status set to 'In progress'.  In a sense, the status
change cascades down to the related objects.

Note that this cascade ignores restrictions from the
``WSHOP_LINE_STATUS_PIPELINE``.

``WSHOP_LINE_STATUS_PIPELINE``
------------------------------

Default: ``{}``

Same as ``WSHOP_ORDER_STATUS_PIPELINE`` but for lines.

Checkout settings
=================

``WSHOP_ALLOW_ANON_CHECKOUT``
-----------------------------

Default: ``False``

Specifies if an anonymous user can buy products without creating an account
first.  If set to ``False`` users are required to authenticate before they can
checkout (using Wshop's default checkout views).

``WSHOP_REQUIRED_ADDRESS_FIELDS``
---------------------------------

Default: ``('first_name', 'last_name', 'line1', 'line4', 'postcode', 'country')``

List of form fields that a user has to fill out to validate an address field.

Review settings
===============

``WSHOP_ALLOW_ANON_REVIEWS``
----------------------------

Default: ``True``

This setting defines whether an anonymous user can create a review for
a product without registering first. If it is set to ``True`` anonymous
users can create product reviews.

``WSHOP_MODERATE_REVIEWS``
--------------------------

Default: ``False``

This defines whether reviews have to be moderated before they are publicly
available. If set to ``False`` a review created by a customer is immediately
visible on the product page.

Communication settings
======================

``WSHOP_EAGER_ALERTS``
----------------------

Default: ``True``

This enables sending alert notifications/emails instantly when products get
back in stock by listening to stock record update signals this might impact
performance for large numbers stock record updates.
Alternatively, the management command ``wshop_send_alerts`` can be used to
run periodically, e.g. as a cronjob. In this case instant alerts should be
disabled.

``WSHOP_SEND_REGISTRATION_EMAIL``
---------------------------------

Default: ``True``

Sending out *welcome* messages to a user after they have registered on the
site can be enabled or disabled using this setting. Setting it to ``True``
will send out emails on registration.

``WSHOP_FROM_EMAIL``
--------------------

Default: ``wshop@example.com``

The email address used as the sender for all communication events and emails
handled by Wshop.

``WSHOP_STATIC_BASE_URL``
-------------------------

Default: ``None``

A URL which is passed into the templates for communication events.  It is not
used in Wshop's default templates but could be used to include static assets
(eg images) in a HTML email template.

Offer settings
==============

``WSHOP_OFFER_ROUNDING_FUNCTION``
---------------------------------

Default: Round down to the nearest hundredth of a unit using ``decimal.Decimal.quantize``

A function responsible for rounding decimal amounts when offer discount
calculations don't lead to legitimate currency values.

Basket settings
===============

``WSHOP_BASKET_COOKIE_LIFETIME``
--------------------------------

Default: 604800 (1 week in seconds)

The time to live for the basket cookie in seconds.

``WSHOP_MAX_BASKET_QUANTITY_THRESHOLD``
---------------------------------------

Default: ``10000``

The maximum number of products that can be added to a basket at once. Set to 
``None`` to disable the basket treshold limitation.


``WSHOP_BASKET_COOKIE_OPEN``
----------------------------

Default: ``'wshop_open_basket'``

The name of the cookie for the open basket.

Currency settings
=================

``WSHOP_DEFAULT_CURRENCY``
--------------------------

Default: ``GBP``

This should be the symbol of the currency you wish Wshop to use by default.
This will be used by the currency templatetag.

.. _currency-format-setting:

``WSHOP_CURRENCY_FORMAT``
-------------------------

Default: ``None``

Dictionary with arguments for the ``format_currency`` function from the `Babel library`_.
Contains next options: `format`, `format_type`, `currency_digits`.
For example::

    WSHOP_CURRENCY_FORMAT = {
        'USD': {
            'currency_digits': False,
            'format_type': "accounting",
        },
        'EUR': {
            'format': u'#,##0\xa0¤',
        }
    }

.. _`Babel library`: http://babel.pocoo.org/en/latest/api/numbers.html#babel.numbers.format_currency

Upload/media settings
=====================

``WSHOP_IMAGE_FOLDER``
----------------------

Default: ``images/products/%Y/%m/``

The location within the ``MEDIA_ROOT`` folder that is used to store product images.
The folder name can contain date format strings as described in the `Django Docs`_.

.. _`Django Docs`: https://docs.djangoproject.com/en/stable/ref/models/fields/#filefield

``WSHOP_DELETE_IMAGE_FILES``
----------------------------

Default: ``True``

If enabled, a ``post_delete`` hook will attempt to delete any image files and
created thumbnails when a model with an ``ImageField`` is deleted. This is
usually desired, but might not be what you want when using a remote storage.


``WSHOP_PROMOTION_FOLDER``
--------------------------

Default: ``images/promotions/``

The folder within ``MEDIA_ROOT`` used for uploaded promotion images.

.. _missing-image-label:

``WSHOP_MISSING_IMAGE_URL``
---------------------------

Default: ``image_not_found.jpg``

Copy this image from ``wshop/static/img`` to your ``MEDIA_ROOT`` folder. It needs to
be there so Sorl can resize it.

``WSHOP_UPLOAD_ROOT``
---------------------

Default: ``/tmp``

The folder is used to temporarily hold uploaded files until they are processed.
Such files should always be deleted afterwards.

Slug settings
=============

``WSHOP_SLUG_MAP``
------------------

Default: ``{}``

A dictionary to map strings to more readable versions for including in URL
slugs.  This mapping is appled before the slugify function.
This is useful when names contain characters which would normally be
stripped.  For instance::

    WSHOP_SLUG_MAP = {
        'c++': 'cpp',
        'f#': 'fsharp',
    }

``WSHOP_SLUG_FUNCTION``
-----------------------

Default: ``'wshop.core.utils.default_slugifier'``

The slugify function to use.  Note that is used within Wshop's slugify wrapper
(in ``wshop.core.utils``) which applies the custom map and blacklist. String
notation is recommended, but specifying a callable is supported for
backwards-compatibility.

Example::

    # in myproject.utils
    def some_slugify(value):
        return value

    # in settings.py
    WSHOP_SLUG_FUNCTION = 'myproject.utils.some_slugify'


``WSHOP_SLUG_BLACKLIST``
------------------------

Default: ``[]``

A list of words to exclude from slugs.

Example::

    WSHOP_SLUG_BLACKLIST = ['the', 'a', 'but']

``WSHOP_SLUG_ALLOW_UNICODE``
----------------------------

Default: ``False``

Allows unicode characters in slugs generated by ``AutoSlugField``,
which is supported by the underlying ``SlugField`` in Django>=1.9.


Dynamic importer settings
=========================

``WSHOP_DYNAMIC_CLASS_LOADER``
----------------------------------

Default: ``wshop.core.loading.default_class_loader``

A dotted path to the callable used to dynamically import classes.


Misc settings
=============

``WSHOP_COOKIES_DELETE_ON_LOGOUT``
----------------------------------

Default: ``['wshop_recently_viewed_products',]``

Which cookies to delete automatically when the user logs out.

``WSHOP_GOOGLE_ANALYTICS_ID``
-----------------------------

Tracking ID for Google Analytics tracking code, available as `google_analytics_id` in the template
context. If setting is set, enables Universal Analytics tracking code for page views and
transactions.


``WSHOP_USE_LESS``
------------------

Allows to use raw LESS styles directly. Refer to :ref:`less-css` document for more details.


``WSHOP_CSV_INCLUDE_BOM``
-------------------------

Default: ``False``

A flag to control whether Wshop's CSV writer should prepend a byte order mark
(BOM) to CSV files that are encoded in UTF-8. Useful for compatibility with some
CSV readers, Microsoft Excel in particular.
