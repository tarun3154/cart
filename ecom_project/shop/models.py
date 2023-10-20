from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='product/')    
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):  
        return self.title

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.title} - Quantity: {self.quantity}"