from django.db import models
from django.conf import settings
from store.models import Product
# Create your models here.

class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'Cart of {self.user.username}'
    def get_total_cost(self):
        return sum(item.get_total_price() for item in self.items.all())



class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items',on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='cart_items',on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} of {self.product.name}'
    
    def get_total_price(self):
        return self.product.price * self.quantity

