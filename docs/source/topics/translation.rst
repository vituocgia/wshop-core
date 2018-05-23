===========
Translation
===========

All Wshop translation work is done on Transifex_. If you'd like to contribute,
just apply for a language and go ahead!
The source strings in Transifex are updated after every commit on Wshop's
master branch on GitHub. We only pull the translation strings back into Wshop's
repository when preparing for a release. That means your most recent
translations will always be on Transifex, not in the repo!

.. _Transifex: https://www.transifex.com/projects/p/wshop-core/


Translating Wshop within your project
-------------------------------------

If Wshop does not provide translations for your language, or if you want to
provide your own, do the following.

Within your project, create a locale folder and a symlink to Wshop so that
``./manage.py makemessages`` finds Wshop's translatable strings::

    mkdir locale i18n
    ln -s $PATH_TO_WSHOP i18n/wshop
    ./manage.py makemessages --symlinks --locale=de

This will create the message files that you can now translate.
