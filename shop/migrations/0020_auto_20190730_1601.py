# Generated by Django 2.2.2 on 2019-07-30 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_auto_20190730_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='zip_code',
            field=models.PositiveIntegerField(db_index=True, verbose_name='ZIP'),
        ),
    ]
