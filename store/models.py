from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

    name = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.name


class Product(models.Model):

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products"
    )

    name = models.CharField(
        max_length=200
    )

    image = models.ImageField(
        upload_to="products/"
    )

    description = models.TextField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    discount = models.PositiveIntegerField(
        default=0
    )

    stock = models.PositiveIntegerField(
        default=0
    )

    # Show this product in Popular Products
    is_popular = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    @property
    def discounted_price(self):

        return self.price - (
            self.price * self.discount / 100
        )

    @property
    def discount_amount(self):

        return self.price - self.discounted_price

    def __str__(self):
        return self.name


class Order(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    full_name = models.CharField(
        max_length=100
    )

    address = models.TextField()

    phone = models.CharField(
        max_length=20
    )

    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    status = models.CharField(
        max_length=20,
        default="Pending"
    )

    def __str__(self):

        return f"Order #{self.id} - {self.user.username}"