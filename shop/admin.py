from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin

from .models import *



class YTUrlsInline(admin.TabularInline):
    model = YTUrls
    raw_id_fields = ['name']

class InstagramImageInline(admin.TabularInline):
    model = InstagramImags
    raw_id_fields = ['name']


class BlogersAdmin(SummernoteModelAdmin):
    # def get_queryset(self, request):
    #     qs = super(BlogersAdmin, self).get_queryset(request)
    #     if request.user.is_superuser:
    #         return qs
    #     return qs.filter(user=request.user)
    # def save_model(self, request, obj, form, change):
    #     obj.user = request.user
    #     # super(BlogersAdmin, self).save_model(request, obj, form, change)
    #     super().save_model(request, obj, form, change)
    list_display = ['name', 'general_image', 'bottom_image', 'title', 'body', 'slug']
    # exclude = ['user', ]
    summernote_fields = '__all__'
    inlines = [YTUrlsInline, InstagramImageInline]


class CategoryAdmin(SummernoteModelAdmin):
    list_display = ['name', 'slug']
    summernote_fields = '__all__'


class ProductAdmin(SummernoteModelAdmin):
    def get_queryset(self, request):
        qs = super(ProductAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    # def save_mode(self, request, obj, form, change):
    #     obj.blogers = Blogers.objects.all().first()
    #     super().save_mode(request, obj, form, change)
    list_display = [
                    'user',
                    # 'blogers',
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
    exclude = ['user', ]
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


class ShirtSubscriptionAdmin(SummernoteModelAdmin):
    pass

class AddressAdmin(admin.ModelAdmin):
    pass



admin.site.register(Blogers, BlogersAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ShirtSubscription, ShirtSubscriptionAdmin)
admin.site.register(Address, AddressAdmin)
