import mock
import os
import tempfile

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import TestCase, override_settings

from wshop.apps.catalogue.abstract_models import MissingProductImage
from wshop.test import factories


class TestProductImages(TestCase):

    def test_images_are_in_consecutive_order(self):
        product = factories.create_product()
        for i in range(4):
            factories.create_product_image(product=product, display_order=i)

        product.images.all()[2].delete()

        for idx, im in enumerate(product.images.all()):
            self.assertEqual(im.display_order, idx)

    def test_variant_images(self):
        parent = factories.ProductFactory(structure='parent')
        variant = factories.create_product(parent=parent)
        factories.create_product_image(product=variant, caption='Variant Image')
        all_images = variant.get_all_images()
        self.assertEquals(all_images.count(), 1)
        product_image = all_images.first()
        self.assertEquals(product_image.caption, 'Variant Image')

    def test_variant_images_fallback_to_parent(self):
        parent = factories.ProductFactory(structure='parent')
        variant = factories.create_product(parent=parent)
        factories.create_product_image(product=parent, caption='Parent Product Image')
        all_images = variant.get_all_images()
        self.assertEquals(all_images.count(), 1)
        product_image = all_images.first()
        self.assertEquals(product_image.caption, 'Parent Product Image')


class TestMissingProductImage(StaticLiveServerTestCase):

    TEMP_MEDIA_ROOT = tempfile.mkdtemp()

    @override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
    @mock.patch('wshop.apps.catalogue.abstract_models.find')
    def test_symlink_creates_directories(self, mock_find):
        # Create a fake empty file to symlink
        img = tempfile.NamedTemporaryFile(delete=False)
        img.close()

        mock_find.return_value = img.name
        # Initialise the class with a nested path
        path = 'image/path.jpg'
        MissingProductImage(path)
        # Check that the directory exists
        image_path = os.path.join(self.TEMP_MEDIA_ROOT, path)
        self.assertTrue(os.path.exists(image_path))

        # Clean up
        for f in [image_path, img.name]:
            os.unlink(f)
        for d in [os.path.join(self.TEMP_MEDIA_ROOT, 'image'), self.TEMP_MEDIA_ROOT]:
            os.rmdir(d)

    @mock.patch('wshop.apps.catalogue.abstract_models.MissingProductImage.symlink_missing_image')
    def test_no_symlink_when_no_media_root(self, mock_symlink):
        MissingProductImage()
        self.assertEqual(mock_symlink.call_count, 0)
