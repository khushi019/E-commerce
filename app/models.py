from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    category_name=models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

class ProductCategory(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    product_category=models.CharField(max_length=100)
    

    def __str__(self):
        return self.product_category
    
class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    product=models.ForeignKey(ProductCategory,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.IntegerField()
    image=models.ImageField(upload_to='images/',validators=[FileExtensionValidator(['png','jpg','jpeg'])])

    def __str__(self):
        return self.name
      

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} in {self.user.username}'s cart"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    city = models.CharField(max_length=50)
    zip = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=[
        ('Pending', 'Pending'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),], default='Pending')  


    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def total_price(self):
        return self.quantity * self.price


    def __str__(self):
        return f"{self.quantity} of {self.product.name} in order {self.order.id}"    