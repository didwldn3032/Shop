# Generated by Django 3.1 on 2020-08-09 19:40

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0002_auto_20200810_0133'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='Review',
        ),
    ]
