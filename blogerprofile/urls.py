from django.urls import path, include
from .views import *


app_name = 'bloger'

urlpatterns = [
    path('<slug>/', profile, name='bloger_profile_p'),
    path('<bloger_slug>/<category_slug>/products/', product_list_p, name='product_list_p'),
    path('bloger-store/products/', bloger_products_p, name='bloger_products_p'),
    path('product/<slug>/', product_detail_p, name='product_detail_p'),
]