from django.contrib import admin
from core.apps.products.models import Product, Category, ProductImage, ProductStock, ProductVariant


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    readonly_fields = ('sku', 'stock')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'base_price', 'status', 'category')
    inlines = [ProductImageInline, ProductVariantInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'use_as_menu')


@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    search_fields = ('sku', 'variant_name', 'product__name')


@admin.register(ProductStock)
class ProductStockAdmin(admin.ModelAdmin):
    list_display = ('product_variant', 'quantity')
    autocomplete_fields = ('product_variant',)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        varient = obj.product_variant
        varient.stock += obj.quantity
        varient.save()