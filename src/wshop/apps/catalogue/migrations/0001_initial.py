# Generated by Django 2.0.5 on 2018-05-23 03:30

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import wshop.core.validators
import wshop.models.fields
import wshop.models.fields.autoslugfield
import wshop.models.fields.slugfield


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttributeOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=255, verbose_name='Option')),
            ],
            options={
                'verbose_name': 'Attribute option',
                'verbose_name_plural': 'Attribute options',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AttributeOptionGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Attribute option group',
                'verbose_name_plural': 'Attribute option groups',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255, unique=True)),
                ('depth', models.PositiveIntegerField()),
                ('numchild', models.PositiveIntegerField(default=0)),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='Name')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to='categories', verbose_name='Image')),
                ('slug', wshop.models.fields.slugfield.SlugField(max_length=255, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['path'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('code', wshop.models.fields.autoslugfield.AutoSlugField(blank=True, editable=False, max_length=128, populate_from='name', unique=True, verbose_name='Code')),
                ('type', models.CharField(choices=[('Required', 'Required - a value for this option must be specified'), ('Optional', 'Optional - a value for this option can be omitted')], default='Required', max_length=128, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Option',
                'verbose_name_plural': 'Options',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('structure', models.CharField(choices=[('standalone', 'Stand-alone product'), ('parent', 'Parent product'), ('child', 'Child product')], default='standalone', max_length=10, verbose_name='Product structure')),
                ('upc', wshop.models.fields.NullCharField(help_text='Universal Product Code (UPC) is an identifier for a product which is not specific to a particular  supplier. Eg an ISBN for a book.', max_length=64, unique=True, verbose_name='UPC')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(max_length=255, verbose_name='Slug')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('rating', models.FloatField(editable=False, null=True, verbose_name='Rating')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('date_updated', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Date updated')),
                ('is_discountable', models.BooleanField(default=True, help_text='This flag indicates if this product can be used in an offer or not', verbose_name='Is discountable?')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ['-date_created'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('code', models.SlugField(max_length=128, validators=[django.core.validators.RegexValidator(message="Code can only contain the letters a-z, A-Z, digits, and underscores, and can't start with a digit.", regex='^[a-zA-Z_][0-9a-zA-Z_]*$'), wshop.core.validators.non_python_keyword], verbose_name='Code')),
                ('type', models.CharField(choices=[('text', 'Text'), ('integer', 'Integer'), ('boolean', 'True / False'), ('float', 'Float'), ('richtext', 'Rich Text'), ('date', 'Date'), ('datetime', 'Datetime'), ('option', 'Option'), ('multi_option', 'Multi Option'), ('entity', 'Entity'), ('file', 'File'), ('image', 'Image')], default='text', max_length=20, verbose_name='Type')),
                ('required', models.BooleanField(default=False, verbose_name='Required')),
                ('option_group', models.ForeignKey(blank=True, help_text='Select an option group if using type "Option" or "Multi Option"', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_attributes', to='catalogue.AttributeOptionGroup', verbose_name='Option Group')),
            ],
            options={
                'verbose_name': 'Product attribute',
                'verbose_name_plural': 'Product attributes',
                'ordering': ['code'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductAttributeValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_text', models.TextField(blank=True, null=True, verbose_name='Text')),
                ('value_integer', models.IntegerField(blank=True, null=True, verbose_name='Integer')),
                ('value_boolean', models.NullBooleanField(verbose_name='Boolean')),
                ('value_float', models.FloatField(blank=True, null=True, verbose_name='Float')),
                ('value_richtext', models.TextField(blank=True, null=True, verbose_name='Richtext')),
                ('value_date', models.DateField(blank=True, null=True, verbose_name='Date')),
                ('value_datetime', models.DateTimeField(blank=True, null=True, verbose_name='DateTime')),
                ('value_file', models.FileField(blank=True, max_length=255, null=True, upload_to='images/products/%Y/%m/')),
                ('value_image', models.ImageField(blank=True, max_length=255, null=True, upload_to='images/products/%Y/%m/')),
                ('entity_object_id', models.PositiveIntegerField(blank=True, editable=False, null=True)),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.ProductAttribute', verbose_name='Attribute')),
                ('entity_content_type', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attribute_values', to='catalogue.Product', verbose_name='Product')),
                ('value_multi_option', models.ManyToManyField(blank=True, related_name='multi_valued_attribute_values', to='catalogue.AttributeOption', verbose_name='Value multi option')),
                ('value_option', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogue.AttributeOption', verbose_name='Value option')),
            ],
            options={
                'verbose_name': 'Product attribute value',
                'verbose_name_plural': 'Product attribute values',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.Category', verbose_name='Category')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.Product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Product category',
                'verbose_name_plural': 'Product categories',
                'ordering': ['product', 'category'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('slug', wshop.models.fields.autoslugfield.AutoSlugField(blank=True, editable=False, max_length=128, populate_from='name', unique=True, verbose_name='Slug')),
                ('requires_shipping', models.BooleanField(default=True, verbose_name='Requires shipping?')),
                ('track_stock', models.BooleanField(default=True, verbose_name='Track stock levels?')),
                ('options', models.ManyToManyField(blank=True, to='catalogue.Option', verbose_name='Options')),
            ],
            options={
                'verbose_name': 'Product class',
                'verbose_name_plural': 'Product classes',
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original', models.ImageField(max_length=255, upload_to='images/products/%Y/%m/', verbose_name='Original')),
                ('caption', models.CharField(blank=True, max_length=200, verbose_name='Caption')),
                ('display_order', models.PositiveIntegerField(default=0, help_text='An image with a display order of zero will be the primary image for a product', verbose_name='Display order')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='catalogue.Product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Product image',
                'verbose_name_plural': 'Product images',
                'ordering': ['display_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductRecommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ranking', models.PositiveSmallIntegerField(default=0, help_text='Determines order of the products. A product with a higher value will appear before one with a lower ranking.', verbose_name='Ranking')),
                ('primary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='primary_recommendations', to='catalogue.Product', verbose_name='Primary product')),
                ('recommendation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.Product', verbose_name='Recommended product')),
            ],
            options={
                'verbose_name': 'Product recommendation',
                'verbose_name_plural': 'Product recomendations',
                'ordering': ['primary', '-ranking'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='productattribute',
            name='product_class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attributes', to='catalogue.ProductClass', verbose_name='Product type'),
        ),
        migrations.AddField(
            model_name='product',
            name='attributes',
            field=models.ManyToManyField(help_text='A product attribute is something that this product may have, such as a size, as specified by its class', through='catalogue.ProductAttributeValue', to='catalogue.ProductAttribute', verbose_name='Attributes'),
        ),
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(through='catalogue.ProductCategory', to='catalogue.Category', verbose_name='Categories'),
        ),
        migrations.AddField(
            model_name='product',
            name='parent',
            field=models.ForeignKey(blank=True, help_text="Only choose a parent product if you're creating a child product.  For example if this is a size 4 of a particular t-shirt.  Leave blank if this is a stand-alone product (i.e. there is only one version of this product).", null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='catalogue.Product', verbose_name='Parent product'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_class',
            field=models.ForeignKey(blank=True, help_text='Choose what type of product this is', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='products', to='catalogue.ProductClass', verbose_name='Product type'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_options',
            field=models.ManyToManyField(blank=True, help_text="Options are values that can be associated with a item when it is added to a customer's basket.  This could be something like a personalised message to be printed on a T-shirt.", to='catalogue.Option', verbose_name='Product options'),
        ),
        migrations.AddField(
            model_name='product',
            name='recommended_products',
            field=models.ManyToManyField(blank=True, help_text='These are products that are recommended to accompany the main product.', through='catalogue.ProductRecommendation', to='catalogue.Product', verbose_name='Recommended products'),
        ),
        migrations.AddField(
            model_name='attributeoption',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='catalogue.AttributeOptionGroup', verbose_name='Group'),
        ),
        migrations.AlterUniqueTogether(
            name='productrecommendation',
            unique_together={('primary', 'recommendation')},
        ),
        migrations.AlterUniqueTogether(
            name='productcategory',
            unique_together={('product', 'category')},
        ),
        migrations.AlterUniqueTogether(
            name='productattributevalue',
            unique_together={('attribute', 'product')},
        ),
        migrations.AlterUniqueTogether(
            name='attributeoption',
            unique_together={('group', 'option')},
        ),
    ]
