# Generated by Django 2.2.2 on 2019-07-26 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='featured',
            field=models.BooleanField(blank=True, default=False, verbose_name='Особенные продукты:'),
        ),
    ]
