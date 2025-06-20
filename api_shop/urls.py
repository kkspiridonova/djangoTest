from django.urls import path, include
from rest_framework import routers

from .views import (
    ClothrsViewSet,
    PosOrderViewSet,
    OrderViewSet,
    CollectionViewSet,
    CategoryViewSet
)

router = routers.DefaultRouter()
router.register('clothes', ClothrsViewSet, basename='clothes')
router.register('pos-orders', PosOrderViewSet, basename='pos-order')
router.register('orders', OrderViewSet, basename='order')
router.register('collections', CollectionViewSet, basename='collection')
router.register('categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls)),
]