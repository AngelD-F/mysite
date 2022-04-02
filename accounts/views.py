from django.shortcuts import render
from django.http import HttpResponse

from .models import *
# Create your views here.

def home(request):
    return render(request, 'accounts/dashboard.html')

def products(request):
    products = product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})

def customer(request):
    return render(request, 'accounts/customer.html')