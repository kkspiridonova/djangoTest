from rest_framework import serializers
from firstproject.models import Category, Collection, Clothrs, Order, Pos_order

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name',
            'description'
        ]

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = [
            'name',
            'description'
        ]

class ClothesSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(
        label='Price',
        max_digits=10,
        decimal_places=2,
        coerce_to_string=False
    )

    class Meta:
        model = Clothrs
        fields = [
            'name',
            'description',
            'price',
            'colour',
            'size',
            'photo',
            'create_data',
            'is_exist',
            'collection',
            'category'
        ]

class PosOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pos_order
        fields = [
            'clothes',
            'order',
            'count',
            'discount'
        ]

class OrderSerializer(serializers.ModelSerializer):
    clothes = PosOrderSerializer(many=True, read_only=True)
    date_create = serializers.DateTimeField(format="%d.%m.%Y %H:%M", read_only=True)
    date_finish = serializers.DateTimeField(format="%d.%m.%Y %H:%M", read_only=True)
    
    class Meta:
        model = Order
        fields = [
            'buyer_firstname',
            'buyer_name',
            'buyer_surname',
            'comment',
            'delivery_address',
            'delivery_type',
            'date_create',
            'date_finish',
            'clothes'
        ]