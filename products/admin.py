from django.contrib import admin
from .models import Category, Subcategory, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'image_preview')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('name',)


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'slug', 'image_preview')
    search_fields = ('name', 'slug', 'category__name')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('category',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'subcategory', 'created_at', 'updated_at')
    list_filter = ('subcategory', 'created_at')
    search_fields = ('name', 'subcategory__name')
    prepopulated_fields = {'slug': ('name',)}
