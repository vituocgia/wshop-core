=====================
Sample Wshop projects
=====================

Wshop ships with one sample project: a 'sandbox' site, which is a vanilla
install of Wshop using the default templates and styles.

The sandbox site
----------------

The sandbox site is a minimal implementation of Wshop where everything is left
in its default state.  It is useful for exploring Wshop's functionality
and developing new features.

It only has one notable customisation on top of Wshop's core:

* A profile class is specified which defines a few simple fields.  This is to
  demonstrate the account section of Wshop, which introspects the profile class
  to build a combined User and Profile form.

Note that some things are deliberately not implemented within core Wshop as they
are domain-specific.  For instance:

* All tax is set to zero.
* No shipping methods are specified.  The default is free shipping which will
  be automatically selected during checkout (as it's the only option).
* No payment is required to submit an order as part of the checkout process.

The sandbox is, in effect, the blank canvas upon which you can build your site.

Browse the external sandbox site
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An instance of the sandbox site is built hourly from master branch and made
available at http://latest.diep.space 

.. warning::
    
    It is possible for users to access the dashboard and edit the site content.
    Hence, the data can get quite messy.  It is periodically cleaned up.


Run the sandbox locally
~~~~~~~~~~~~~~~~~~~~~~~

It's pretty straightforward to get the sandbox site running locally so you can
play around with Wshop.

.. warning::
    
    While installing Wshop is straightforward, some of Wshop's dependencies
    don't support Windows and are tricky to be properly installed, and therefore
    you might encounter some errors that prevent a successful installation.
    
Install Wshop and its dependencies within a virtualenv:

.. code-block:: bash

    $ git clone https://github.com/vituocgia/wshop-core.git
    $ cd wshop-core
    $ mkvirtualenv wshop  # needs virtualenvwrapper
    (wshop) $ make sandbox
    (wshop) $ sandbox/manage.py runserver

.. warning::
    
    Note, these instructions will install the head of Wshop's 'master' branch,
    not an official release. Occasionally the sandbox installation process
    breaks while support for a new version of Django is being added (often due
    dependency conflicts with 3rd party libraries). Please ask on the mailing
    list if you have problems.

If you do not have ``mkvirtualenv``, then replace that line with:

.. code-block:: bash

    $ virtualenv wshop
    $ source ./wshop/bin/activate
    (wshop) $

The sandbox site (initialised with a sample set of products) will be available
at: http://localhost:8000.  A sample superuser is installed with credentials::

    username: superuser
    email: superuser@example.com
    password: testing
