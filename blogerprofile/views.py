from django.shortcuts import render, get_object_or_404

from blogerstore import shop
from .models import *
from django.http import HttpResponseRedirect

import json

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def profile(request, slug):
    blogers = shop.models.Blogers.objects.all()

    bloger_profile = get_object_or_404(BlogerProfile, slug=slug)

    blogerprofile = BlogerProfile.objects.get(slug=slug)
    blogercategory = BlogerCategory.objects.filter(bloger=blogerprofile)
    blogerproduct = BlogerProduct.objects.filter(available=True)

    context = {
        'bloger_profile': bloger_profile,
        'blogercategory': blogercategory,
        'blogers': blogers,
        'blogerproduct': blogerproduct,
        'blogerprofile': blogerprofile,
    }

    return render(request, 'blogerprofile/profile.html', context=context)

def product_list_p(request, bloger_slug, category_slug):
    blogers = shop.models.Blogers.objects.all()

    blogerprofile = BlogerProfile.objects.filter(slug=bloger_slug)
    blogercategory = BlogerCategory.objects.filter(slug=category_slug)
    blogerproduct = BlogerProduct.objects.filter(available=True)

    context = {
        'blogers': blogers,
        'blogerprofile': blogerprofile,
        'blogerproduct': blogerproduct,
        'blogercategory': blogercategory,
    }

    return render(request, 'blogerprofile/product_list.html', context=context)

def product_detail_p(request, slug):
    blogers = shop.models.Blogers.objects.all()

    blogerproduct = BlogerProduct.objects.filter(available=True, slug=slug)

    context = {
        'blogers': blogers,
        # 'bloger': bloger,
        'blogerproduct': blogerproduct,
        # 'category': category,
    }

    return render(request, 'blogerprofile/product_detail.html', context=context)



def bloger_products_p(request):
    blogers = shop.models.Blogers.objects.all()

    blogerproduct = BlogerProduct.objects.all().filter(available=True)

    context = {
        'blogers': blogers,
        'blogerproduct': blogerproduct,
    }

    return render(request, 'blogerprofile/bloger_products.html', context=context)



