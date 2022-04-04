from django.shortcuts import render, get_object_or_404
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

    ctx = {'products': products}

    return render(request, 'accounts/products.html', ctx)


def customer(request, pk):
    customer = get_object_or_404(mdl.customer, id=pk)
    c_orders = customer.order_set.all()
    c_total = c_orders.count()

    ctx = {'customer': customer, 'orders': c_orders, 'orders_total':c_total}

    return render(request, 'accounts/customer.html', ctx)


def create_order(request):
    ctx = {}
    
    return render(request, 'accounts/order_form.html', ctx)

