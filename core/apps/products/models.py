import uuid
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    use_as_menu = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    def get_products(self):
        return self.products.all()


class Product(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ]
    name = models.CharField(max_length=255)
    description = models.TextField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    specifications = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')   

    def __str__(self):
        return self.name
    
    