=================
Customising Wshop
=================

Many parts of Wshop can be adapted to your needs like any other Django
application:

* Many :doc:`settings</ref/settings>` control Wshop's behavior
* The looks can be controlled by extending or overriding the
  :doc:`templates </howto/how_to_customise_templates>`

But as Wshop is built as a highly customisable and extendable framework, it
doesn't stop there. The behaviour of all Wshop apps can heavily be altered
by injecting your own code.

To extend the behavior of an Wshop core app, it needs to be forked, which is
achieved with a simple management command. Afterwards, you should
generally be able to override any class/model/view by just dropping it
in the right place and giving it the same name.

In some cases, customising is slightly more involved. The following how-tos
give plenty of examples for specific use cases:

* :doc:`/howto/how_to_customise_models`
* :doc:`/howto/how_to_change_a_url`
* :doc:`/howto/how_to_customise_a_view`

For a deeper understanding of customising Wshop, the following documents are
recommended:

* :doc:`/internals/design-decisions`
* :doc:`Dynamic class loading</topics/class_loading_explained>`
* :doc:`fork_app`

.. _fork-wshop-app:

Fork the Wshop app
==================

If this is the first time you're forking an Wshop app, you'll need to create
a root module under which all your forked apps will live::

    $ mkdir yourappsfolder
    $ touch yourappsfolder/__init__.py

Now you call the helper management command which creates some basic files for
you. It is explained in detail in :doc:`fork_app`. Run it like this::

    $ ./manage.py wshop_fork_app order yourappsfolder/
    Creating folder apps/order
    Creating __init__.py and admin.py
    Creating models.py and copying migrations from [...] to [...]

.. note::

   For forking app in project root directory, call ``wshop_fork_app`` with ``.`` (dot) instead of ``yourproject/`` path.
   
   Example: 
   
   Calling ``./manage.py wshop_fork_app order yourproject/`` ``order`` app will be placed in ``project_root/yourproject/`` directory. 
   Calling ``./manage.py wshop_fork_app order .`` ``order`` app will be placed in ``project_root/`` directory.

Replace Wshop's app with your own in ``INSTALLED_APPS``
=======================================================

You will need to let Django know that you replaced one of Wshop's core
apps. You can do that by supplying an extra argument to
``get_core_apps`` function::

    # settings.py

    from wshop import get_core_apps
    # ...
    INSTALLED_APPS = [
        # all your non-Wshop apps
    ] + get_core_apps(['yourappsfolder.order'])

``get_core_apps([])`` will return a list of Wshop core apps. If you supply a
list of additional apps, they will be used to replace the Wshop core apps.
In the above example, ``yourproject.order`` will be returned instead of
``wshop.apps.order``.

.. note::

    Overrides of dashboard applications should follow overrides of core
    applications (basket, catalogue etc), since they depend on models,
    declared in the core applications. Otherwise, it could cause issues
    with Wshop's dynamic model loading.

    Example:

    .. code:: django

        INSTALLED_APPS = [
            # all your non-Wshop apps
        ] + get_core_apps([
            # core applications
            'yourappsfolder.catalogue',
            'yourappsfolder.order',
            # dashboard applications
            'yourappsfolder.dashboard',
            'yourappsfolder.dashboard.orders',
            'yourappsfolder.dashboard.reports',
        ])


Start customising!
==================

You can now override every class (that is
:doc:`dynamically loaded </topics/class_loading_explained>`, which is
almost every class) in the app you've replaced. That means forms,
views, strategies, etc. All you usually need to do is give it the same name
and place it in a module with the same name.

Suppose you want to alter the way order numbers are generated.  By default,
the class ``wshop.apps.order.utils.OrderNumberGenerator`` is used. So just
create a class within your ``order`` app which
matches the module path from wshop: ``order.utils.OrderNumberGenerator``.  This
could subclass the class from Wshop or not::

    # yourproject/order/utils.py

    from wshop.apps.order.utils import OrderNumberGenerator as CoreOrderNumberGenerator


    class OrderNumberGenerator(CoreOrderNumberGenerator):

        def order_number(self, basket=None):
            num = super(OrderNumberGenerator, self).order_number(basket)
            return "SHOP-%s" % num
