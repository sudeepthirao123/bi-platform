
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
