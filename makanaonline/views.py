from django.shortcuts import render
#from django.shortcuts import get_object_or_404
from .models import *


def store(request):
    products = Product.objects.all()
    return render(request, 'store.html', {'products': products})


def cart(request):
    context = {}
    return render(request, 'cart.html', {'context': context})


def checkout(request):
    context = {}
    return render(request, 'checkout.html', {'context': context})
