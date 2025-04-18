from django.urls import path
from core.api.v1.products.views import (
    MenuApiView,
    ProductListApiView,
    ProductByCategoryApiView,
    ProductDetailApiView
)
urlpatterns = [
    path('menu/', MenuApiView.as_view(), name='menu'),
    path('', ProductListApiView.as_view(), name='product-list'),
    path('category/<str:category_name>/', ProductByCategoryApiView.as_view(), name='product-by-category'),
    path('<int:id>/', ProductDetailApiView.as_view(), name='product-detail'),
]

