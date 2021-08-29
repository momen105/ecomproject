from django.shortcuts import render

# Import views
from django.views.generic import ListView, DetailView

# Models
from Home_App.models.product_model import Product

# Mixin
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class Home(ListView):
    model = Product
    template_name = 'home.html'

class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'shop_templates/product_detail.html'

