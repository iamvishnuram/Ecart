from django.db import models
from store.models import Product

class Cart(models.Model):
    cartid = models.CharField(max_length=50, blank=True)
    date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'cart'
        ordering = ['date']
        
    def __str__(self):
        return '{}'.format(self.cartid)
    
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'CartItem'
    def sub_total(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return '{}'.format(self.product)
    
    

# Create your models here.
