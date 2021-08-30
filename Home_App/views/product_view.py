from django.shortcuts import render

# Import views
from django.views.generic import ListView, DetailView
from django.views import View
# Models
from Home_App.models.product_model import Product, Category

# Mixin
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class Home(View):
    def get(self, request):
        products = None
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products()
        data = {}
        data['products'] = products
        data['categories'] = categories
        return render(request, 'home.html', data)


class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'shop_templates/product_detail.html'
