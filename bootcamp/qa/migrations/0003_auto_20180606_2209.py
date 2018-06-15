# Generated by Django 2.0.3 on 2018-06-06 22:09

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('qa', '0002_auto_20180605_1603'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together={('user', 'content_type', 'object_id')},
        ),
    ]