==================
Core functionality
==================

This page details the core classes and functions that Wshop uses.  These aren't
specific to one particular app, but are used throughout Wshop's codebase.

Dynamic class loading
---------------------

The key to Wshop's flexibility is dynamically loading classes.  This allows
projects to provide their own versions of classes that extend and override the
core functionality.

.. automodule:: wshop.core.loading
    :members: get_classes, get_class

URL patterns and views
----------------------

Wshop's app organise their URLs and associated views using a "Application"
class instance.  This works in a similar way to Django's admin app, and allows
Wshop projects to subclass and customised URLs and views.

.. automodule:: wshop.core.application
    :members:

Prices
------

Wshop uses a custom price object for easier tax handling.

.. automodule:: wshop.core.prices
    :members: Price

Custom model fields
-------------------

Wshop uses a few custom model fields.

.. automodule:: wshop.models.fields
    :members:


Form helpers
------------

.. automodule:: wshop.forms.mixins
    :members:
