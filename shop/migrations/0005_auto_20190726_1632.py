# Generated by Django 2.2.2 on 2019-07-26 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20190726_1630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shirtsubscription',
            name='bloger',
        ),
        migrations.RemoveField(
            model_name='shirtsubscription',
            name='category',
        ),
    ]
