from rest_framework import serializers
from core.apps.products.models import Product, Category, ProductImage, ProductVariant


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'use_as_menu']
        read_only_fields = ['id']

