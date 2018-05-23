from django.test import TestCase
from django.template import loader, TemplateDoesNotExist

import wshop


class TestWshopCoreAppsList(TestCase):

    def test_includes_wshop_itself(self):
        core_apps = wshop.WSHOP_CORE_APPS
        self.assertTrue('wshop' in core_apps)

    def test_can_be_retrieved_through_fn(self):
        core_apps = wshop.get_core_apps()
        self.assertTrue('wshop' in core_apps)

    def test_can_be_retrieved_with_overrides(self):
        apps = wshop.get_core_apps(overrides=['apps.shipping'])
        self.assertTrue('apps.shipping' in apps)
        self.assertTrue('wshop.apps.shipping' not in apps)

    def test_raises_exception_for_string_arg(self):
        with self.assertRaises(ValueError):
            wshop.get_core_apps('forks.catalogue')


class TestWshopTemplateSettings(TestCase):
    """
    Wshop's WSHOP_MAIN_TEMPLATE_DIR setting
    """
    def test_allows_a_template_to_be_accessed_via_two_paths(self):
        paths = ['base.html', 'wshop/base.html']
        for path in paths:
            try:
                loader.get_template(path)
            except TemplateDoesNotExist:
                self.fail("Template %s should exist" % path)

    def test_allows_a_template_to_be_customized(self):
        path = 'base.html'
        template = loader.get_template(path)
        rendered_template = template.render({})
        self.assertIn('Wshop Test Shop', rendered_template)

    def test_default_wshop_templates_are_accessible(self):
        path = 'wshop/base.html'
        template = loader.get_template(path)
        rendered_template = template.render({})
        self.assertNotIn('Wshop Test Shop', rendered_template)
