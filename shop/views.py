from django.shortcuts import render, get_object_or_404
from .models import *
from cart.forms import CartAddProductForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from django.http import HttpResponseRedirect

import blogerprofile

import json

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



def shop(request):
    blogers = Blogers.objects.all()

    product = Product.objects.all().filter(available=True)
    blogerproduct = blogerprofile.models.BlogerProduct.objects.all().filter(available=True)

    if request.GET.get('name', ''):
        name = request.GET.get('name', '')
        mail = request.GET.get('mail', '')
        soc_url = request.GET.get('soc_url', '')
        follawers = request.GET.get('follawers', '')
        text = request.GET.get('text', '')

        data = {
            'name': name,
            'mail': mail,
            'soc_url': soc_url,
            'follawers': follawers,
            'text': text,
        }

        result = json.dumps(data, indent=4)

        email_user = 'hystyle2019@gmail.com'
        email_send = 'artush.ghazaryan96@gmail.com'
        subject = 'GET BRENDED'

        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_send
        msg['Subject'] = subject

        msg.attach(MIMEText(result, 'plain'))
        text = msg.as_string()

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_user, 'LKJHGFDSA31')
        server.sendmail(email_user, email_send, text)
        return HttpResponseRedirect('/')





    context = {
        'blogers': blogers,
        'product': product,
        'blogerproduct': blogerproduct,
    }

    return render(request, 'shop/base_shop.html', context=context)



def sale(request):
    blogers = Blogers.objects.all()
    product = Product.objects.all().filter(available=True, sale_on=True)


    context = {
        'blogers': blogers,
        'product': product,
    }

    return render(request, 'shop/sale.html', context=context)



def subscrib(request):
    blogers = Blogers.objects.all()

    subscrib = ShirtSubscription.objects.all().filter(available=True)


    context = {
        'blogers': blogers,
        'subscrib': subscrib,
    }
    return render(request, 'shop/subscription.html', context=context)

def subscrib_detail(request, id):
    blogers = Blogers.objects.all()

    subscrib = ShirtSubscription.objects.all().filter(available=True, id=id)


    context = {
        'blogers': blogers,
        'subscrib': subscrib,
    }
    return render(request, 'shop/sub_detail.html', context=context)


def blogers(request):
    blogers = Blogers.objects.all()

    return render(request, 'shop/blogers.html', context={'blogers': blogers})


def blogers_profile(request, slug):
    blogers = Blogers.objects.all()

    bloger_profile = get_object_or_404(Blogers, slug=slug)

    bloger = Blogers.objects.get(slug=slug)
    category = Category.objects.filter(bloger=bloger)
    product = Product.objects.filter(available=True)

    context = {
        'bloger_profile': bloger_profile,
        'category': category,
        'blogers': blogers,
        'product': product,
        'bloger': bloger,
    }

    return render(request, 'shop/profile.html', context=context)





def product_list(request, bloger_slug, category_slug):
    blogers = Blogers.objects.all()

    bloger = Blogers.objects.filter(slug=bloger_slug)
    category = Category.objects.filter(slug=category_slug)
    product = Product.objects.filter(available=True)

    context = {
        'blogers': blogers,
        'bloger': bloger,
        'product': product,
        'category': category,
    }

    return render(request, 'shop/product_list.html', context=context)


def new_arrivals(request):
    blogers = Blogers.objects.all()

    product = Product.objects.filter(available=True)

    context = {
        'blogers': blogers,
        'product': product,
    }

    return render(request, 'shop/new_arrivals.html', context=context)

def featured_products(request):
    blogers = Blogers.objects.all()

    product = Product.objects.filter(available=True, featured=True)

    context = {
        'blogers': blogers,
        'product': product,
    }

    return render(request, 'shop/featured_products.html', context=context)

def product_detail(request, id):
    blogers = Blogers.objects.all()
    cart_product_form = CartAddProductForm()
    product = Product.objects.filter(available=True, id=id)

    context = {
        'blogers': blogers,
        # 'bloger': bloger,
        'product': product,
        'cart_product_form': cart_product_form,
    }

    return render(request, 'shop/product_detail.html', context=context)


def user_profile(request):



    return  render(request, 'account/user_profile.html')

def user_address(request):


    return render(request, 'account/address.html')





