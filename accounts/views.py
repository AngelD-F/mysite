from django.shortcuts import render
from django.http import HttpResponse

from . import models as mdl
# Create your views here.

def home(request):
    orders = mdl.order.objects.all()
    customers = mdl.customer.objects.all()

    ctx = {'orders': orders, 'customers': customers}

    return render(request, 'accounts/dashboard.html', ctx)

def products(request):
    products = mdl.product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})

def customer(request):
    return render(request, 'accounts/customer.html')