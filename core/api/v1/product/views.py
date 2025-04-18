from rest_framework import generics
from core.apps.products.models import Product, Category, ProductImage, ProductVariant
from core.apps.products.serializers import (
    ProductSerializer,
    CategorySerializer,
    ProductImageSerializer,
    ProductVariantSerializer,
)


class MenuApiView(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(use_as_menu=True)


class ProductListApiView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductByCategoryApiView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_name = self.kwargs.get['category_name']
        return Product.objects.filter(category_name_iexact=category_name)
    

class ProductDetailApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'