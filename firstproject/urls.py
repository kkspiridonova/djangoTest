from django.urls import path, include 
from .views import *

urlpatterns = [
    path('info', info_view, name="info_view"),
    path('', info_view),
    path('clothes/',ClothrListView.as_view(), name='clothes_list'),
    path('clothes/<int:pk>/',ClothrListDetailView.as_view(), name='clothes_detail'),
    path('clothes/create/',ClothrListCreateView.as_view(), name='clothes_create'),
    path('clothes/<int:pk>/update',ClothrListUpdateView.as_view(), name='clothes_update'),
    path('clothes/<int:pk>/delete',ClothrListDeleteView.as_view(), name='clothes_delete'),
    path('catalog/', catalog_page, name='catalog'),
]
