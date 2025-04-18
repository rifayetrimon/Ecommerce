import uuid
from django.db import models

# Create your models here.

class Category(models.Model): # Category model
    name = models.CharField(max_length=255)
    use_as_menu = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    def get_products(self):
        return self.products.all()


class Product(models.Model): # Product model
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
    

class ProductImage(models.Model): # Product Image model
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.product.name}"


class ProductVariant(models.Model): # Product Variant model
    product = models.ForeignKey(Product, related_name='variants', on_delete=models.CASCADE)
    variant_name = models.CharField(max_length=255)
    attributes = models.JSONField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=50, blank=True)
    size = models.CharField(max_length=50, blank=True)
    stock = models.PositiveIntegerField(default=0)
    sku = models.CharField(max_length=20, blank=True, null=True, unique=True)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.product.name} - {self.variant_name}"
    
    def save (self, *args, **kwargs):
        if not self.sku:
            self.sku = uuid.uuid4().hex[:10].upper()
        super().save(*args, **kwargs)

class ProductStock(models.Model): # Product Stock model
    product_variant = models.ForeignKey(ProductVariant, related_name='stocks', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self, *args, **kwargs):
        return f"{self.product_variant.sku}"