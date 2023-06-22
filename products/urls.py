from django.urls import path
from .views import ProductView, ProductDetailsView

urlpatterns = [
    path('products/', ProductView.as_view()),
    path('products/<int:product_id>/', ProductDetailsView.as_view()),
]