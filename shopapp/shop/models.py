from django.db import models
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    image_url = models.URLField(max_length=1000, blank=True, 
        default="https://via.placeholder.com/300x200?text=Product+Image")

    def __str__(self):
        return self.name
    
    def get_formatted_price(self):
        return f"${self.price:,.2f}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    stripe_payment_intent = models.CharField(max_length=200, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    line_items = models.JSONField(default=list)
    status = models.CharField(max_length=20, default='pending')

    def __str__(self):
        return f"Order {self.id} - {self.total_amount}"
