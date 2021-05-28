from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    price = models.IntegerField(default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    stock = models.IntegerField(default=100, blank=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=5, blank=True)
    imageUrl = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title


class Order(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivered = models.BooleanField(default=False, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.product) + ' | ' + str(self.user)
