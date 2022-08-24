from django.contrib import admin
from .models import Product, Category

# Register models to appear in the admin
admin.site.register(Product)
admin.site.register(Category)
