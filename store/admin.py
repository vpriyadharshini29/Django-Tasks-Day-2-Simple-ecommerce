from django.contrib import admin
from .models import Product, Category, Order

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'in_stock')
    list_filter = ('in_stock', 'category')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    filter_horizontal = ('products',)
