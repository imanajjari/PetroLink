from django.contrib import admin
from .models import ProductModel, ProductImageModel, ProductCategoryModel,WishlistProductModel,ProductFileModel,PlantType,CurrencyType,ProcessUnit,EquipmentType,DisciplineType

# Register your models here.

@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "stock", "status","price","discount_percent", "created_date", "savingMony")

@admin.register(ProductCategoryModel)
class ProductCategoryModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_date")

@admin.register(PlantType)
class ProductCategoryModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_date")

@admin.register(CurrencyType)
class ProductCategoryModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_date")

@admin.register(ProcessUnit)
class ProductCategoryModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_date")

@admin.register(EquipmentType)
class ProductCategoryModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_date")

@admin.register(DisciplineType)
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

