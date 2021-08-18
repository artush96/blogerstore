from django.urls import path, include
from .views import *

app_name = 'shop'

urlpatterns = [
    path('', shop, name='shop_list'),
    path('new-arrivles/', new_arrivals, name='new_arrivals'),
    path('featured-products/', featured_products, name='featured_products'),
    path('sale/', sale),
    path('bloger/', blogers, name='blogers'),
    path('bloger/<slug>/', blogers_profile, name='bloger_profile'),
    path('<bloger_slug>/<category_slug>/products/', product_list, name='product_list'),
    path('product/<id>/', product_detail, name='product_detail'),
    path('shirtsubscription/', subscrib, name='subscrib'),
    path('shirtsubscription/<id>/', subscrib_detail, name='subscrib_detail'),
    path('accounts/profile/', user_profile, name='user_profile'),
    path('accounts/address/', user_address, name='user_address'),
]
