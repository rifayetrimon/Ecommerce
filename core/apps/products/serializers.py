from rest_framework import serializers
from core.apps.products.models import Product, Category, ProductImage, ProductVariant


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'use_as_menu']
        read_only_fields = ['id']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'caption']
        read_only_fields = ['id']


class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = ['id', 'variant_name', 'attributes', 'price', 'color', 'size', 'stock', 'sku', 'image']
        read_only_fields = ['id', 'sku']


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, required=False, read_only=True)
    variants = ProductVariantSerializer(many=True, required=False, read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'base_price', 'specifications', 'category', 'status', 'images', 'variants']
        read_only_fields = ['id', 'category']