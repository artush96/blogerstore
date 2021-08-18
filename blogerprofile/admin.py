from django.contrib import admin
from .models import *

from django_summernote.admin import SummernoteModelAdmin

class YTUrlsInline(admin.TabularInline):
    model = YTUrls
    raw_id_fields = ['name']

class InstagramImageInline(admin.TabularInline):
    model = InstagramImags
    raw_id_fields = ['name']


class BlogerProfileAdmin(SummernoteModelAdmin):
    list_display = [
        'name',
        'slug'

    ]
    summernote_fields = '__all__'
    inlines = [YTUrlsInline, InstagramImageInline]


class BlogerCategoryAdmin(SummernoteModelAdmin):
    list_display = ['name', 'slug']
    summernote_fields = '__all__'


class BlogerProductAdmin(SummernoteModelAdmin):
    list_display = [
                    'category',
                    'name',
                    'slug',
                    'size_s',
                    'size_m',
                    'size_l',
                    'size_xl',
                    'size_2xl',
                    'size_3xl',
                    'price',
                    'sale_on',
                    'sale',
                    'available',
    ]
    list_editable = [
                    'price',
                    'sale_on',
                    'sale',
                    'size_s',
                    'size_m',
                    'size_l',
                    'size_xl',
                    'size_2xl',
                    'size_3xl',
                    'available',
    ]
    summernote_fields = '__all__'





admin.site.register(BlogerProfile, BlogerProfileAdmin)
admin.site.register(BlogerCategory, BlogerCategoryAdmin)
admin.site.register(BlogerProduct, BlogerProductAdmin)