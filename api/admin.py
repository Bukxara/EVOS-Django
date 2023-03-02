from django.contrib import admin
from .models import UsersModel, CategoryModel, ProductModel, BasketModel, OrderModel
# Register your models here.

admin.site.register(UsersModel)
admin.site.register(CategoryModel)
admin.site.register(ProductModel)
admin.site.register(BasketModel)
admin.site.register(OrderModel)
