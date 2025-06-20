from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from firstproject.models import Clothrs, Order, Pos_order
from .basket import Basket
from .forms import BasketAddProductForm, OrderForm

def basket_detail(request):
    """Отображение содержимого корзины"""
    basket = Basket(request)
    return render(request, 'basket/detail.html', {'basket': basket})

@require_POST
def basket_remove(request, product_id):
    """Удаление товара из корзины"""
    basket = Basket(request)
    product = get_object_or_404(Clothrs, pk=product_id)
    basket.remove(product)
    return redirect('basket_detail')

def basket_clear(request):
    """Полная очистка корзины"""
    basket = Basket(request)
    basket.clear()
    return redirect('basket_detail')

@require_POST
@login_required
def basket_add(request, product_id):
    """Добавление товара в корзину"""
    basket = Basket(request)
    product = get_object_or_404(Clothrs, pk=product_id)
    form = BasketAddProductForm(request.POST)

    if form.is_valid():
        basket.add(
            product=product,
            count=form.cleaned_data['count'],
            update_count=form.cleaned_data['reload']
        )
        return redirect('basket_detail')

@login_required
def basket_buy(request):
    """Оформление заказа из корзины"""
    basket = Basket(request)

    if len(basket) <= 0:
        return redirect('list_product.filter')

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(
                buyer_firstname=form.cleaned_data['buyer_firstname'],
                buyer_name=form.cleaned_data['buyer_name'],
                buyer_surname=form.cleaned_data['buyer_surname'],
                comment=form.cleaned_data['comment'],
                delivery_address=form.cleaned_data['delivery_address'],
                delivery_type=form.cleaned_data['delivery_type'],
                price=basket.get_total_price()
            )

            for item in basket:
                Pos_order.objects.create(
                    clothes=item['product'],
                    count=item['count'],
                    order=order,
                    discount=0
                )
            
            basket.clear()
            return redirect('info_view')
        
        return redirect('info_view')

@login_required
def open_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            return redirect('info_view')
    else:
        form = OrderForm()
    
    context = {
        'form_order': form,
        'basket': Basket(request)
    }
    return render(request, 'order/order_form.html', context)