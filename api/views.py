from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import UsersModel, CategoryModel, ProductModel, BasketModel, OrderModel
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.


class UsersView(APIView):
    serializer_class = UserSerializers

    def get(self, request, tg_id):
        try:
            data = UsersModel.objects.filter(telegram_id=tg_id)
        except UsersModel.DoesNotExist:
            return Response({"message": "Не найдено!"}, status=status.HTTP_404_NOT_FOUND)
        if data:
            serializer = UserSerializers(data, many=True)
            return Response(serializer.data)
        return Response({"message": "Не найдено!"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, tg_id):
        try:
            info = UsersModel.objects.get(telegram_id=tg_id)
        except UsersModel.DoesNotExist:
            return Response({"message": "Не найдено!"}, status=status.HTTP_404_NOT_FOUND)
        if info:
            serializer = UsersUpdateSerializers(info, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Обновлено!"}, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors)


class CategoryView(ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializers
    

class CategoryViewByName(APIView):

    def get(self, request, name):
        data = CategoryModel.objects.filter(category_name = name)
        serializer = CategorySerializers(data, many=True)
        return Response(serializer.data)


class ProductView(ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializers


class ProductViewByName(APIView):
    def get(self, request, name):
        data = ProductModel.objects.filter(product_name=name)
        serializer = ProductSerializers(data, many=True)
        return Response(serializer.data)


class AllCategories(APIView):
    def get(self, request):
        data = CategoryModel.objects.all()
        serializer = CategorySerializers(data, many=True)
        return Response(serializer.data)


class ProductsByCategoryId(APIView):

    def get(self, request, pk):
        data = ProductModel.objects.filter(category_id=pk)
        serializer = ProductSerializers(data, many=True)
        return Response(serializer.data)


class ProductsByCategoryName(APIView):

    def get(self, request, name):
        data = ProductModel.objects.filter(category_name=name)
        serializer = ProductSerializers(data, many=True)
        return Response(serializer.data)
    

class BasketView(ModelViewSet):
    queryset = BasketModel.objects.all()
    serializer_class = BasketSerializers


class BasketByUser(APIView):

    def delete(self, request, tg_id):
        data = BasketModel.objects.filter(telegram_id=tg_id)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, tg_id):
        data = BasketModel.objects.filter(telegram_id=tg_id)
        serializer = BasketSerializers(data, many=True)
        return Response(serializer.data)


class OrderView(APIView):

    def get(self, request, tg_id):
        data = OrderModel.objects.filter(telegram_id=tg_id)
        if data:
            serializer = OrderSerializers(data, many=True)
            return Response(serializer.data)
        return Response({"message": "База данных пуста!"}, status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "PUT", "DELETE"])
def upgrade(request, tg_id, product_id):
    try:
        snippet = BasketModel.objects.get(
            telegram_id=tg_id, product_id=product_id)
    except BasketModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        if snippet:
            serializer = BasketSerializers(snippet)
            return Response(serializer.data)
        return Response({'message': "Не найдено!"}, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'PUT':
        serializer = BasketUpdateSerializers(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Обновлено!"}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors)

    elif request.method == 'DELETE':
        if snippet:
            snippet.delete()
            return Response({"message": "Удалено!"})
        return Response(serializer.errors)

    return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["GET", "POST", "PUT"])
def post_users(request):
    if request.method == "POST":
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Добавлено!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    elif request.method == "GET":
        data = UsersModel.objects.all()
        if data:
            serializer = UserSerializers(data, many=True)
            return Response(serializer.data)
        return Response({"message": "База данных пуста"}, status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
def post_order(request):
    serializer = OrderSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Добавлено!"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors)
