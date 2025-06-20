from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets
from firstproject.models import *
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser


class ClothrsViewSet(viewsets.ModelViewSet):
    """ViewSet для работы с товарами (Clothes)"""
    queryset = Clothrs.objects.all()
    serializer_class = ClothesSerializer

class OrderViewSet(viewsets.ModelViewSet):
    """ViewSet для работы с заказами (Order)"""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser] 


class PosOrderViewSet(viewsets.ModelViewSet):
    """ViewSet для работы с позициями заказов (Pos_order)"""
    queryset = Pos_order.objects.all()
    serializer_class = PosOrderSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    """ViewSet для работы с категориями (Category)"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CollectionViewSet(viewsets.ModelViewSet):
    """ViewSet для работы с коллекциями (Collection)"""
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer