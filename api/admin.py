from django.contrib import admin
from .models import UsersModel, CategoryModel, ProductModel, BasketModel
# Register your models here.

admin.site.register(UsersModel)
admin.site.register(CategoryModel)
admin.site.register(ProductModel)
admin.site.register(BasketModel)
