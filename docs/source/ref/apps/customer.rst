========
Customer
========

The customer app bundles communication with customers. This includes models
to record product alerts and sent emails. It also contains the views that
allow a customer to manage their data (profile information, shipping addresses,
etc.)

Abstract models
---------------

.. automodule:: wshop.apps.customer.abstract_models
    :members:

Forms
-----

.. automodule:: wshop.apps.customer.forms
    :members:

Views
-----

.. automodule:: wshop.apps.customer.views
    :members:

Alerts
------

The alerts module provides functionality that allows customers to sign up for
email alerts when out-of-stock products come back in stock. A form for signing
up is displayed on product detail pages when a product is not in stock.

If the ``WSHOP_EAGER_ALERTS` setting is ``True``, then alerts are sent as soon
as affected stock records are updated. Alternatively, the management command
``wshop_send_alerts`` can be used to send alerts periodically.

The context for the alert email body contains a ``hurry`` variable that is set
to ``True`` if the number of active alerts for a product is greater than the
quantity of the product available in stock.

Alerts are sent using the Communication Event framework.
