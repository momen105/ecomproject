from django.contrib import admin
from Home_App.models.product_model import Category, Product


# Register your models here.

admin.site.register(Category)
admin.site.register(Product)