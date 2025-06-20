from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from basket.forms import BasketAddProductForm, OrderForm
from .models import *
from .forms import *

def info_view(request):
    return render(request, "info.html")

class ClothrListView(ListView):
    model = Clothrs
    template_name = 'clothes/clothes_list.html'
    context_object_name = 'clothes'

class ClothrListDetailView(DetailView):
    model = Clothrs
    template_name = 'clothes/clothes_detail.html'
    context_object_name = 'clothes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_basket"] = BasketAddProductForm(
            initial={
                'count': 1,
                'reload': False
            }
        )
        return context
            

class ClothrListCreateView(CreateView):
    model = Clothrs
    form_class = ClothrsForm
    template_name = 'clothes/clothes_form.html'
    success_url = reverse_lazy('clothes_list')

class ClothrListUpdateView(UpdateView):
    model = Clothrs
    form_class = ClothrsForm
    template_name = 'clothes/clothes_form.html'
    success_url = reverse_lazy('clothes_list')

class ClothrListDeleteView(DeleteView):
    model = Clothrs
    template_name = 'clothes/clothes_delete.html'
    success_url = reverse_lazy('clothes_list')

from django.contrib.auth.decorators import permission_required
from django.shortcuts import render

@permission_required('shop.add_product')
def is_able_to_add_product(request):
    """Проверка права на добавление товаров"""
    return render(request, 'shop/can_add_product.html')

@permission_required(['shop.add_product', 'shop.change_product'])
def is_able_to_add_and_change_product(request):
    """Проверка права на добавление и изменение товаров"""
    return render(request, 'shop/can_add_change_product.html')

@permission_required('shop.change_delivery_type')
def is_able_to_change_delivery_type(request):
    """Проверка права на изменение способа доставки"""
    return render(request, 'shop/can_change_delivery_type.html')

def open_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return ('info')  # замените на нужный URL после успешного сохранения
    else:
        form = OrderForm()

    return render(request, 'order/order_form.html', {'form': form})


def catalog_page(request):
    return render(request, 'catalog.html')