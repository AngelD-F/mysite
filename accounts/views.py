from django.shortcuts import render
from django.http import HttpResponse

from . import models as mdl
# Create your views here.

def home(request):
    orders = mdl.order.objects.all()
    customers = mdl.customer.objects.all()

    total_orders = orders.count()
    total_pending_orders = orders.filter(status='Pending').count()
    total_delivered_orders = orders.filter(status='Delivered').count()

    ctx = {
        'orders': orders, 
        'customers': customers,
        'total_orders': total_orders,
        'total_pending': total_pending_orders,
        'total_delivered': total_delivered_orders
    }

    return render(request, 'accounts/dashboard.html', ctx)

def products(request):
    products = mdl.product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})

def customer(request):
    return render(request, 'accounts/customer.html')