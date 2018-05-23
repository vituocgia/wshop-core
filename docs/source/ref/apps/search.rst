======
Search
======

Wshop provides a search view that extends Haystack's ``FacetedSearchView`` to
provide better support for faceting.  

* Facets are configured using the ``WSHOP_SEARCH_FACETS`` setting, which is
  used to configure the ``SearchQuerySet`` instance within the search
  application class.

* A simple search form is injected into each template context using a context
  processor ``wshop.apps.search.context_processors.search_form``.

Views
-----

.. automodule:: wshop.apps.search.views
    :members:

Forms
-----

.. automodule:: wshop.apps.search.forms
    :members:

Utils
-----

.. automodule:: wshop.apps.search.facets
    :members:
