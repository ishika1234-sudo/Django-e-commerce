from django.db import models
from product.models import Product, Variation

# Create your models here.
class Cart(models.Model):
    cart_id = models.CharField(max_length=250)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.cart_id)

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation = models.ManyToManyField(Variation, blank=True) # there can be same product with multiple colors and sizes
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def sub_qty(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return str(self.product)