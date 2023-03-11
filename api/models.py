from django.db import models
from django.urls import reverse

# Create your models here.


class UsersModel(models.Model):
    username = models.CharField(max_length=50)
    telegram_id = models.CharField(max_length=50)
    user_address = models.JSONField(max_length=200, null=True)
    phone_number = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.username


class CategoryModel(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    category_image = models.ImageField(upload_to="images/", blank=True)

    def __str__(self):
        return self.category_name


class ProductModel(models.Model):
    category_id = models.ForeignKey(
        CategoryModel, on_delete=models.SET_NULL, null=True)
    category_name = models.ForeignKey(
        CategoryModel, to_field="category_name", on_delete=models.SET_NULL, null=True, related_name="category")
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


class OrderModel(models.Model):

    telegram_id = models.CharField(max_length=50)
    order_items = models.CharField(max_length=1000)
    payment_method = models.CharField(max_length=20)
    order_status = models.CharField(max_length=100, null=True)
    order_address = models.JSONField(max_length=200, null=True)
    order_sum = models.CharField(max_length=100)

    # def save(self, *args, **kwargs):
    #     user = OrderModel.objects.all().filter(telegram_id=self.telegram_id)
    #     if len(user) == 5:
    #         us = OrderModel.objects.all().filter(telegram_id=self.telegram_id).first()
    #         us.delete()
    #     super(OrderModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.telegram_id


class CommentModel(models.Model):
    telegram_id = models.CharField(max_length=50)
    username = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()

    def __str__(self):
        return f"{self.username}'s comment"
