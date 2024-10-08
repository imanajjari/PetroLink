from django.contrib import admin
from .models import ProductModel, ProductImageModel, ProductCategoryModel,WishlistProductModel,ProductFileModel,PlantType

# Register your models here.

@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "stock", "status","price","discount_percent", "created_date")

@admin.register(ProductCategoryModel)
class ProductCategoryModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_date")

@admin.register(PlantType)
class ProductCategoryModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_date")

@admin.register(ProductImageModel)
class ProductImageModelAdmin(admin.ModelAdmin):
    list_display = ("id", "file", "created_date")

@admin.register(ProductFileModel)
class ProductFileModellAdmin(admin.ModelAdmin):
    list_display = ("id", "file", "created_date")

@admin.register(WishlistProductModel)
class WishlistProductModelAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "product")

