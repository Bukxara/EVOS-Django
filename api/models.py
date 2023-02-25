from django.db import models
from django.urls import reverse

# Create your models here.


class UsersModel(models.Model):
    username = models.CharField(max_length=50)
    telegram_id = models.CharField(max_length=50)
    language = models.CharField(max_length=2, blank=True)

    def __str__(self):
        return self.username


class CategoryModel(models.Model):
    category_name = models.CharField(max_length=50)
    category_image = models.ImageField(upload_to="images/", blank=True)

    def __str__(self):
        return self.category_name


class ProductModel(models.Model):
    category_id = models.ForeignKey(
        CategoryModel, on_delete=models.SET_NULL, null=True)
    product_name = models.CharField(max_length=50)
    product_price = models.IntegerField()
    product_description = models.TextField(blank=True)
    product_image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse("shop", args=[str(self.id)])


class BasketModel(models.Model):
    telegram_id = models.CharField(max_length=50)
    product_id = models.CharField(max_length=9)
    product_count = models.IntegerField()

    def __str__(self):
        return self.telegram_id
