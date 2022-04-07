from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory

from . import models as mdl
from .forms import orderForm
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
        'total_delivered': total_delivered_orders,
    }
    return render(request, 'accounts/dashboard.html', ctx)


def products(request):
    products = mdl.product.objects.all()

    ctx = {
        'activeNav': 1,
        'products': products,
    }
    return render(request, 'accounts/products.html', ctx)


def customer(request, pk):
    customer = get_object_or_404(mdl.customer, id=pk)
    c_orders = customer.order_set.all()
    c_total = c_orders.count()

    ctx = {'customer': customer, 'orders': c_orders, 'orders_total':c_total}
    return render(request, 'accounts/customer.html', ctx)


def create_order(request, pk):
    orderFormSet = inlineformset_factory(
        mdl.customer, 
        mdl.order, 
        fields=('product', 'status'),
        extra=5
    )
    customer = get_object_or_404(mdl.customer, id=pk)
    formset = orderFormSet(queryset=mdl.order.objects.none(), instance=customer)
    if request.method == 'POST':
        # print('Printing POST: ', request.POST)
        formset = orderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    ctx = {'formset': formset}    
    return render(request, 'accounts/order_form.html', ctx)


def update_order(request, pk):
    order = get_object_or_404(mdl.order, id=pk)
    form = orderForm(instance=order)

    if request.method == 'POST':
        form = orderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            url = request.GET.get('next', '/')
            return redirect(url)

    ctx = {'form': form}    
    return render(request, 'accounts/order_form.html', ctx)


def delete_order(request, pk):
    order = get_object_or_404(mdl.order, id=pk)

    if request.method == 'POST':
        order.delete()
        url = request.GET.get('next', '/')
        return redirect(url)

    ctx = {'item': order}
    return render(request, 'accounts/delete.html', ctx)

