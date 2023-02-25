from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializers, CategorySerializers, ProductSerializers, BasketSerializers, BasketUpdateSerializers, UserExistsSerializers
from .models import UsersModel, CategoryModel, ProductModel, BasketModel
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.


class UsersView(ModelViewSet):
    queryset = UsersModel.objects.all()
    serializer_class = UserSerializers


class CategoryView(ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializers


class ProductView(ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializers


class AllCategories(APIView):

    def get(self, request):
        data = CategoryModel.objects.all()
        serializer = CategorySerializers(data, many=True)
        return Response(serializer.data)


class ProductsByCategory(APIView):

    def get(self, request, pk):
        data = ProductModel.objects.filter(category_id=pk)
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
            return Response({"msg": "Обновлено!"})
        return Response(serializer.errors)

    elif request.method == 'DELETE':
        if snippet:
            snippet.delete()
            return Response({"msg": "Удалено!"})
        return Response(serializer.errors)

    return Response(status=status.HTTP_404_NOT_FOUND)
