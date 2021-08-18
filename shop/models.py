from django.db import models
from django.db.models import Model, ForeignKey
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.core.validators import RegexValidator, MaxLengthValidator, MinLengthValidator

from autoslug import AutoSlugField

from django.conf import settings

# class User(AbstractUser):
#     is_bloger = models.BooleanField(default=True)




# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Blogers.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
#
# def update_blogers(request, user_id):
#     user = User.objects.get(pk=user_id)
#     user.profile.name = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
#     user.save()


    # @property
    # def get_absolute_url(self):
    #     return reverse('', args=[self.slug])









class Category(models.Model):
    bloger = models.ForeignKey('Blogers', on_delete=models.CASCADE)
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
        return reverse('shop:product_list', args=[self.slug])


class Product(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    bloger = models.ForeignKey('Blogers', on_delete=models.CASCADE, related_name='products', verbose_name='Влиятельност:')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products', verbose_name='Категория:')
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
        index_together = ('id',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id])


class Blogers(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, related_name='MyUser')
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
        return reverse('shop:bloger_profile', args=[self.slug])

    # def __unicode__(self):
    #     return u'Profile of user: %s' % self.user.username


class YTUrls(models.Model):
    name = models.ForeignKey(Blogers, on_delete=models.CASCADE)
    yt_urls = models.CharField(max_length=1000)


class InstagramImags(models.Model):
    name = models.ForeignKey(Blogers, on_delete=models.CASCADE)
    insta_url = models.CharField(max_length=1000)


class ShirtSubscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200, db_index=True, verbose_name='Название:')
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
        return reverse('shop:subscrib', args=[self.id, self.slug])


from django.core.validators import MaxValueValidator
class Address(models.Model):
    first_name = models.CharField(max_length=15, db_index=True, verbose_name='Имя')
    last_name = models.CharField(max_length=15, db_index=True, verbose_name='Фамилия')
    phone_regex = RegexValidator(regex=r'^\+?7?\d{9,15}$', message="Phone number must be entered in the format:\
                                                                        '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, verbose_name='Телефон')
    company = models.CharField(max_length=20, db_index=True, blank=True, verbose_name='Компания')
    address1 = models.CharField(max_length=40, db_index=True, verbose_name='Адрес 1')
    address2 = models.CharField(max_length=40, db_index=True, blank=True, verbose_name='Адрес 2')
    city = models.CharField(max_length=15, db_index=True, verbose_name='Город')
    country = models.CharField(max_length=15, db_index=True, verbose_name='Страна')
    zip_code = models.PositiveIntegerField(db_index=True, verbose_name='ZIP')

    def __str__(self):
        return self.first_name











