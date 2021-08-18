from django.db import models
from django.db.models import Model, ForeignKey
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

from autoslug import AutoSlugField

from django.conf import settings


class BlogerCategory(models.Model):
    bloger = models.ForeignKey('BlogerProfile', on_delete=models.CASCADE)
    name = models.CharField(max_length=150, db_index=True)
    slug = AutoSlugField(populate_from='name', always_update=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'Категория:'
        verbose_name_plural = 'Категорий:'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('bloger:product_list_p', args=[self.slug])


class BlogerProduct(models.Model):
    bloger = models.ForeignKey('BlogerProfile', on_delete=models.CASCADE, related_name='products', verbose_name='Блогер:')
    category = models.ForeignKey('BlogerCategory', on_delete=models.CASCADE, related_name='products', verbose_name='Категория:')
    name = models.CharField(max_length=200, db_index=True, verbose_name='Название:')
    featured = models.BooleanField(default=False, verbose_name='Особенные продукты:')
    slug = AutoSlugField(populate_from='name', always_update=True, unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name='Изображение товара:')
    description = models.TextField(blank=True, verbose_name="Описание:")
    size_s = models.BooleanField(default=True, verbose_name='S:')
    size_m = models.BooleanField(default=True, verbose_name='M:')
    size_l = models.BooleanField(default=True, verbose_name='L:')
    size_xl = models.BooleanField(default=True, verbose_name='XL:')
    size_2xl = models.BooleanField(default=True, verbose_name='2XL:')
    size_3xl = models.BooleanField(default=True, verbose_name='3XL:')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена:')
    sale_on = models.BooleanField(default=False, blank=True, verbose_name='Роспродажа:')
    sale = models.DecimalField(max_digits=10, blank=True, null=True, decimal_places=2, verbose_name='Цена на скидке:')
    available = models.BooleanField(default=True, blank=True, verbose_name='Доступен:')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('price', )
        verbose_name = ('Прадукти')
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('bloger:product_detail_p', args=[self.id, self.slug])


class BlogerProfile(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = AutoSlugField(populate_from='name', always_update=True, unique=True)
    general_image = models.ImageField(upload_to='blogers/%Y/%m/%d', blank=True)
    bottom_image = models.ImageField(upload_to='blogers/%Y/%m/%d', blank=True)
    title = models.CharField(max_length=40, verbose_name='Title')
    body = models.TextField(max_length=300, verbose_name='Body')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Блогер:'
        verbose_name_plural = 'Блогери:'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('bloger:bloger_profile_p', args=[self.slug])

    # def __unicode__(self):
    #     return u'Profile of user: %s' % self.user.username


class YTUrls(models.Model):
    name = models.ForeignKey(BlogerProfile, on_delete=models.CASCADE)
    yt_urls = models.CharField(max_length=1000)


class InstagramImags(models.Model):
    name = models.ForeignKey(BlogerProfile, on_delete=models.CASCADE)
    insta_url = models.CharField(max_length=1000)



