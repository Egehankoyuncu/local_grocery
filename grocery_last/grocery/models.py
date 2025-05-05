from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Store(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(default='No address provided')
    phone = models.CharField(max_length=20, default='No phone provided')
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='store_images/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.name} at {self.store.name}"

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'product')
    
    def __str__(self):
        return f"{self.user.username}'s favorite: {self.product.name}"
