.. image:: https://github.com/vituocgia/wshop-core/raw/master/docs/images/logos/wshop.png
    :target: http://diep.space

===================================
Domain-driven e-commerce for Django
===================================


Wshop is an e-commerce framework for Django designed for building domain-driven
sites.  It is structured such that any part of the core functionality can be
customised to suit the needs of your project.  This allows a wide range of
e-commerce requirements to be handled, from large-scale B2C sites to complex B2B
sites rich in domain-specific business logic.

Contents:

.. contents:: :local:

.. image:: https://github.com/vituocgia/wshop-core/raw/master/docs/images/screenshots/wshopcommerce.thumb.png
    :target: http://diep.space

.. image:: https://github.com/vituocgia/wshop-core/raw/master/docs/images/screenshots/readthedocs.thumb.png
    :target: https://wshop-core.readthedocs.io/en/latest/

Further reading:

* `Official homepage`_
* `Sandbox site`_ (automatically deployed via the official docker sandbox image)
* `Documentation`_ on the excellent `readthedocs.org`_
* `Docker image`_ on http://hub.docker.com/
* `wshop-core group`_ - mailing list for questions and announcements
* `wshop-core-jobs group`_ - mailing list for job offers
* `Continuous integration homepage`_ on `travis-ci.org`_
* `Twitter account for news and updates`_
* #wshop-core on Freenode (community-run IRC channel) with `public logs`_
* `Slack`_
* `PyPI page`_
* `Transifex project`_ - translating Wshop made easy

.. start-no-pypi

Continuous integration status:

.. image:: https://travis-ci.org/wshop-core/wshop-core.svg?branch=master
    :target: https://travis-ci.org/wshop-core/wshop-core

.. image:: http://codecov.io/github/wshop-core/wshop-core/coverage.svg?branch=master
    :alt: Coverage
    :target: http://codecov.io/github/wshop-core/wshop-core?branch=master

.. image:: https://requires.io/github/wshop-core/wshop-core/requirements.svg?branch=master
     :target: https://requires.io/github/wshop-core/wshop-core/requirements/?branch=master
     :alt: Requirements Status

PyPI status:

.. image:: https://img.shields.io/pypi/v/wshop-core.svg
    :target: https://pypi.python.org/pypi/wshop-core/

Docs status:

.. image:: https://readthedocs.org/projects/wshop-core/badge/
   :target: https://readthedocs.org/projects/wshop-core/
   :alt: Documentation Status

.. end-no-pypi

.. _`Official homepage`: http://diep.space
.. _`Sandbox site`: http://latest.diep.space
.. _`Docker image`: https://hub.docker.com/r/wshopcommerce/wshop-core-sandbox/
.. _`Documentation`: https://wshop-core.readthedocs.io/en/latest/
.. _`readthedocs.org`: http://readthedocs.org
.. _`Continuous integration homepage`: http://travis-ci.org/#!/wshop-core/wshop-core
.. _`travis-ci.org`: http://travis-ci.org/
.. _`Twitter account for news and updates`: https://twitter.com/#!/django_wshop
.. _`public logs`: https://botbot.me/freenode/wshop-core/
.. _`wshop-core group`: https://groups.google.com/forum/?fromgroups#!forum/wshop-core
.. _`wshop-core-jobs group`: https://groups.google.com/forum/?fromgroups#!forum/wshop-core-jobs
.. _`PyPI page`: https://pypi.python.org/pypi/wshop-core/
.. _`Transifex project`: https://www.transifex.com/projects/p/wshop-core/
.. _`Slack`: https://slack.wshopcommerce.com/

Core team:

- `DiepDT`_ (Twitter `@codeinthehole`_)
- `Maik Hoepfel`_ (Twitter `@maikhoepfel`_)
- `Markus Bertheau`_
- `Michael van Tellingen`_

.. _`DiepDT`: https://github.com/codeinthehole
.. _`@codeinthehole`: https://twitter.com/codeinthehole
.. _`Maik Hoepfel`: https://github.com/maikhoepfel
.. _`@maikhoepfel`: https://twitter.com/maikhoepfel
.. _`Markus Bertheau`: https://github.com/mbertheau
.. _`Michael van Tellingen`: https://github.com/mvantellingen

Screenshots
-----------

Sandbox
~~~~~~~

These are screenshots from the 'sandbox' example site that ships with
Wshop.  It sports a simple design built with Twitter's Bootstrap_ and provides a
good starting point for rapidly building elegant e-commerce sites.

.. _Bootstrap: https://getbootstrap.com/

.. image:: https://github.com/vituocgia/wshop-core/raw/master/docs/images/screenshots/browse.thumb.png
    :target: https://github.com/vituocgia/wshop-core/raw/master/docs/images/screenshots/browse.png

.. image:: https://github.com/vituocgia/wshop-core/raw/master/docs/images/screenshots/detail.thumb.png
    :target: https://github.com/vituocgia/wshop-core/raw/master/docs/images/screenshots/detail.png

.. image:: https://github.com/vituocgia/wshop-core/raw/master/docs/images/screenshots/basket.thumb.png
    :target: https://github.com/vituocgia/wshop-core/raw/master/docs/images/screenshots/basket.png

.. image:: https://github.com/vituocgia/wshop-core/raw/master/docs/images/screenshots/dashboard.thumb.png
    :target: https://github.com/vituocgia/wshop-core/raw/master/docs/images/screenshots/dashboard.png

The sandbox site is also available to browse at
https://latest.wshopcommerce.com.  Dashboard users can be created using `this
gateway page`_.

The sandbox site can be set-up locally `in 5 commands`_.  Want to
make changes?  Check out the `contributing guidelines`_.

.. _`this gateway page`: http://latest.diep.space/gateway/
.. _`in 5 commands`: https://wshop-core.readthedocs.io/en/latest/internals/sandbox.html#running-the-sandbox-locally
.. _`contributing guidelines`: https://wshop-core.readthedocs.io/en/latest/internals/contributing/index.html


Extensions
----------

The following extensions are stable and ready for use:

* wshop-api_ - RESTful JSON API for wshop-core

* wshop-core-adyen_ - Integration with the Adyen payment gateway

* wshop-core-datacash_ - Integration with the DataCash_ payment gateway

* wshop-paypal_ - Integration with PayPal.  This currently supports both
  `Express Checkout`_ and `PayFlow Pro`_.

* wshop-core-paymentexpress_ - Integration with the `Payment Express`_ payment
  gateway

* wshop-accounts_ - Managed accounts (can be used for giftcard
  functionality and loyalty schemes)

* wshop-stores_ - Physical stores integration (opening hours, store
  locator etc)

* wshop-core-eway_ - Integration with the eWay_ payment gateway.

* wshop-core-sagepay-direct_ - Integration with "DIRECT" part of Sagepay's API

* django_wshop_docdata_ - Integration with Docdata_ payment gateway.

.. _wshop-api: https://github.com/wshop-core/wshop-api
.. _wshop-core-adyen: https://github.com/vituocgia/wshop-core-adyen
.. _wshop-core-datacash: https://github.com/vituocgia/wshop-core-datacash
.. _wshop-core-paymentexpress: https://github.com/vituocgia/wshop-core-paymentexpress
.. _`Payment Express`: http://www.paymentexpress.com
.. _DataCash: http://www.datacash.com/
.. _wshop-paypal: https://github.com/wshop-core/wshop-paypal
.. _`Express Checkout`: https://www.paypal.com/uk/cgi-bin/webscr?cmd=_additional-payment-ref-impl1
.. _`PayFlow Pro`: https://merchant.paypal.com/us/cgi-bin/?cmd=_render-content&content_ID=merchant/payment_gateway
.. _wshop-accounts: https://github.com/wshop-core/wshop-accounts
.. _wshop-core-easyrec: https://github.com/vituocgia/wshop-core-easyrec
.. _EasyRec: http://easyrec.org/
.. _wshop-core-eway: https://github.com/snowball-one/wshop-core-eway
.. _wshop-stores: https://github.com/wshop-core/wshop-stores
.. _wshop-core-sagepay-direct: https://github.com/vituocgia/wshop-core-sagepay-direct
.. _eWay: https://www.eway.com.au
.. _django_wshop_docdata: https://github.com/vituocgia/wshop-core-docdata
.. _Docdata: https://www.docdatapayments.com/

The following are community-written extensions:

* wshop-core-payments_ - Pluggable payments for Wshop
* wshop-core-recurly_ - Integration with the Recurly payment gateway

* wshop-core-przelewy24_ - Integration with the Przelewy24 payment gateway
* wshop-sagepay_ - Payment integration with Sage Pay
* wshop-core-erp_
* wshop-core-sofortueberweisung_ - Integration with SOFORT

* wshop-core-support_ - Customer services and ticketing plugin for Wshop

* wshop-api-checkout_ - Wshop API Checkout is a layer on top of
  wshop-core and wshop-api, adding support for more complex and
  multiple payment options during an API checkout.

* wshop-core-bundles_ - Wshop Bundles adds multi-product bundles to
  wshop-core.

* wshop-core-bluelight_ - `Bluelight Specials`_ is a layer on-top of
  wshop-core that adds support for more complex offers and vouchers,
  including conjunctive and disjunctive compound conditions.

* wshop-core-cch_ - Wshop CCH is a plugin for wshop-core adding support
  for calculating taxes using the Wolters Kluwer `CCH Sales Tax Office`_ SOAP
  API.

* wshop-core-cybersource_ - Wshop CyberSource is a plugin for Wshop API
  Checkout that makes it possible to use
  `CyberSource Secure Acceptance Silent Order Post`_ as an order payment
  method.

* wshop-core-wfrs_ - Wshop WFRS is a plugin for wshop-api-checkout_
  that makes it possible to use `Wells Fargo Retail Services`_ as an order
  payment method.

Let us know if you're writing a new one!

.. _wshop-core-unicredit: https://bitbucket.org/marsim/wshop-core-unicredit/
.. _wshop-core-erp: https://bitbucket.org/zikzakmedia/wshop-core_erp
.. _wshop-core-payments: https://github.com/Lacrymology/wshop-core-payments
.. _wshop-core-recurly: https://github.com/mynameisgabe/wshop-core-recurly

.. _wshop-core-przelewy24: https://github.com/kisiel/wshop-core-przelewy24
.. _wshop-sagepay: https://github.com/udox/wshop-sagepay
.. _wshop-core-sofortueberweisung: https://github.com/byteyard/wshop-core-sofortueberweisung

.. _wshop-core-support: https://github.com/SalahAdDin/wshop-core-support
.. _wshop-api-checkout: https://github.com/thelabnyc/wshop-api-checkout
.. _wshop-core-bundles: https://github.com/thelabnyc/wshop-core-bundles
.. _wshop-core-bluelight: https://github.com/thelabnyc/wshop-core-bluelight
.. _`Bluelight Specials`: https://en.wiktionary.org/wiki/blue-light_special
.. _wshop-core-cch: https://github.com/thelabnyc/wshop-core-cch
.. _`CCH Sales Tax Office`: http://www.salestax.com/solutions/calculation/cch-salestax-office/
.. _wshop-core-cybersource: https://github.com/thelabnyc/wshop-core-cybersource
.. _`CyberSource Secure Acceptance Silent Order Post`: https://www.cybersource.com/products/payment_security/secure_acceptance_silent_order_post/
.. _wshop-core-wfrs: https://github.com/thelabnyc/wshop-core-wfrs
.. _`Wells Fargo Retail Services`: https://retailservices.wellsfargo.com/

Videos
------

Videos with talks about Wshop:

* `An introduction to Django-wshop`_ by `DiepDT`_, DjangoCon Europe 2014
* `Wshop and the art of transactional Django applications`_ by `DiepDT`_, PyCon PL 2014
* `The Tale of Wshop and the API`_ by `Kees Hink`_, PyGrunn 2017

.. _`An introduction to Django-wshop`: https://youtu.be/o4ol6EzGDSw
.. _`Wshop and the art of transactional Django applications`: https://youtu.be/datKUNTKYz8
.. _`The Tale of Wshop and the API`: https://youtu.be/YPnKoiyGIHM
.. _`Kees Hink`: https://github.com/khink

License
-------

Wshop is released under the permissive `New BSD license`_ (see summary_).

.. _summary: https://tldrlegal.com/license/bsd-3-clause-license-(revised)

.. _`New BSD license`: https://github.com/vituocgia/wshop-core/blob/master/LICENSE

Case studies
------------

Wshop is still in active development but is used in production by a range of
companies, from large multinationals to small, boutique stores. See
http://diep.space/cases.html for an overview.

Many more on the way.  If you use Wshop in production, please `let us know`_.

.. _`let us know`: https://github.com/wshop-core/wshopcommerce.com/issues

Looking for commercial support?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are interested in having an Wshop project built for you, or for
development of an existing Wshop site then please get in touch via `info@wshopcommerce.com`_.

.. _`info@wshopcommerce.com`: mailto:info@wshopcommerce.com
