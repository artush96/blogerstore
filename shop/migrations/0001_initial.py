# Generated by Django 2.2.2 on 2019-07-24 17:02

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='name', unique=True)),
                ('general_image', models.ImageField(blank=True, upload_to='blogers/%Y/%m/%d')),
                ('bottom_image', models.ImageField(blank=True, upload_to='blogers/%Y/%m/%d')),
                ('title', models.CharField(max_length=40, verbose_name='Title')),
                ('body', models.TextField(max_length=300, verbose_name='Body')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='MyUser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Блогер:',
                'verbose_name_plural': 'Блогери:',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150)),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='name', unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('bloger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Blogers')),
            ],
            options={
                'verbose_name': 'Категория:',
                'verbose_name_plural': 'Категорий:',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='YTUrls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yt_urls', models.CharField(max_length=500)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Blogers')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Название:')),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='name', unique=True)),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d', verbose_name='Изображение товара:')),
                ('description', models.TextField(blank=True, verbose_name='Описание:')),
                ('size_s', models.BooleanField(default=True, verbose_name='S:')),
                ('size_m', models.BooleanField(default=True, verbose_name='M:')),
                ('size_l', models.BooleanField(default=True, verbose_name='L:')),
                ('size_xl', models.BooleanField(default=True, verbose_name='XL:')),
                ('size_2xl', models.BooleanField(default=True, verbose_name='2XL:')),
                ('size_3xl', models.BooleanField(default=True, verbose_name='3XL:')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена:')),
                ('sale_on', models.BooleanField(blank=True, default=False, verbose_name='Роспродажа:')),
                ('sale', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Цена на скидке:')),
                ('available', models.BooleanField(blank=True, default=True, verbose_name='Доступен:')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('bloger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.Blogers', verbose_name='Влиятельност:')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.Category', verbose_name='Категория:')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Прадукти',
                'ordering': ('price',),
                'index_together': {('id', 'slug')},
            },
        ),
    ]
