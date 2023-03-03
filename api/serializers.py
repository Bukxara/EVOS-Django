from rest_framework import serializers
from .models import UsersModel, CategoryModel, ProductModel, BasketModel, OrderModel


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = UsersModel
        fields = '__all__'


class UsersUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = UsersModel
        fields = ['phone_number', 'user_address']


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'


class BasketSerializers(serializers.ModelSerializer):
    class Meta:
        model = BasketModel
        fields = '__all__'


class BasketUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = BasketModel
        fields = ['product_count']


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = '__all__'
