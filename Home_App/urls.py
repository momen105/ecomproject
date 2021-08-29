from django.urls import path
from .views.product_view import Home, ProductDetail

app_name = 'Home_App'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('product/<pk>/', ProductDetail.as_view(), name='product_detail'),
]