# Generated by Django 3.1 on 2020-08-10 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_delete_post2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
