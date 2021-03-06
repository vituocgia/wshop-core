# Generated by Django 2.0.5 on 2018-05-23 03:30

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import wshop.models.fields.autoslugfield


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalogue', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CommunicationEventType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', wshop.models.fields.autoslugfield.AutoSlugField(blank=True, editable=False, help_text='Code used for looking up this event programmatically', max_length=128, populate_from='name', separator='_', unique=True, validators=[django.core.validators.RegexValidator(message="Code can only contain the letters a-z, A-Z, digits, and underscores, and can't start with a digit.", regex='^[a-zA-Z_][0-9a-zA-Z_]*$')], verbose_name='Code')),
                ('name', models.CharField(help_text='This is just used for organisational purposes', max_length=255, verbose_name='Name')),
                ('category', models.CharField(choices=[('Order related', 'Order related'), ('User related', 'User related')], default='Order related', max_length=255, verbose_name='Category')),
                ('email_subject_template', models.CharField(blank=True, max_length=255, null=True, verbose_name='Email Subject Template')),
                ('email_body_template', models.TextField(blank=True, null=True, verbose_name='Email Body Template')),
                ('email_body_html_template', models.TextField(blank=True, help_text='HTML template', null=True, verbose_name='Email Body HTML Template')),
                ('sms_template', models.CharField(blank=True, help_text='SMS template', max_length=170, null=True, verbose_name='SMS Template')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date Updated')),
            ],
            options={
                'verbose_name': 'Communication event type',
                'verbose_name_plural': 'Communication event types',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email Address')),
                ('subject', models.TextField(max_length=255, verbose_name='Subject')),
                ('body_text', models.TextField(verbose_name='Body Text')),
                ('body_html', models.TextField(blank=True, verbose_name='Body HTML')),
                ('date_sent', models.DateTimeField(auto_now_add=True, verbose_name='Date Sent')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='emails', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Email',
                'verbose_name_plural': 'Emails',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('category', models.CharField(blank=True, max_length=255)),
                ('location', models.CharField(choices=[('Inbox', 'Inbox'), ('Archive', 'Archive')], default='Inbox', max_length=32)),
                ('date_sent', models.DateTimeField(auto_now_add=True)),
                ('date_read', models.DateTimeField(blank=True, null=True)),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Notification',
                'verbose_name_plural': 'Notifications',
                'ordering': ('-date_sent',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductAlert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, db_index=True, max_length=254, verbose_name='Email')),
                ('key', models.CharField(blank=True, db_index=True, max_length=128, verbose_name='Key')),
                ('status', models.CharField(choices=[('Unconfirmed', 'Not yet confirmed'), ('Active', 'Active'), ('Cancelled', 'Cancelled'), ('Closed', 'Closed')], default='Active', max_length=20, verbose_name='Status')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('date_confirmed', models.DateTimeField(blank=True, null=True, verbose_name='Date confirmed')),
                ('date_cancelled', models.DateTimeField(blank=True, null=True, verbose_name='Date cancelled')),
                ('date_closed', models.DateTimeField(blank=True, null=True, verbose_name='Date closed')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.Product')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='alerts', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Product alert',
                'verbose_name_plural': 'Product alerts',
                'abstract': False,
            },
        ),
    ]
