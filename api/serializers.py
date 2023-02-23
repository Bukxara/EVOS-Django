from rest_framework import serializers
from .models import UsersModel, CategoryModel, ProductModel, BasketModel


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = UsersModel
        fields = '__all__'


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

