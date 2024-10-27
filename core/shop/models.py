from django.db import models
from decimal import Decimal
from django.core.validators import MaxValueValidator, MinValueValidator


class ProductStatusType(models.IntegerChoices):
    publish = 1 ,("نمایش")
    draft = 2 ,("عدم نمایش")

class DisciplineType(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode=True,unique=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-created_date"]
        
    def __str__(self):
        return self.name

class EquipmentType(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode=True,unique=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-created_date"]
        
    def __str__(self):
        return self.name

class PlantType(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode=True,unique=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-created_date"]
        
    def __str__(self):
        return self.name

class ProcessUnit(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode=True,unique=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-created_date"]
        
    def __str__(self):
        return self.name

class CurrencyType(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode=True,unique=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-created_date"]
        
    def __str__(self):
        return self.name


class ProductCategoryModel(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode=True,unique=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-created_date"]
        
    def __str__(self):
        return self.title


# Create your models here.
class ProductModel(models.Model):
    user = models.ForeignKey("accounts.User",on_delete=models.PROTECT)
    category = models.ManyToManyField(ProductCategoryModel)
    title = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode=True,unique=True)
    image = models.ImageField(default="/default/product-image.png",upload_to="product/img/")
    description = models.TextField()
    brief_description = models.TextField(null=True,blank=True)

    # new item 
    # کد کالا
    mesc_code = models.PositiveIntegerField()
    # شماره مدرک
    docNo = models.CharField(max_length=255)
    # تاریخ تهیه مدرک
    docData = models.DateTimeField()
    # شماره ویرایش مدرک
    doc_ver = models.PositiveIntegerField()
    # سازنده اصلی
    vendor = models.CharField(max_length=255)
    # شماره قطعه کارخانه اصلی سازنده
    manufacturerPartNo = models.CharField(max_length=255)
    # شماره قطعه سازنده
    supplierPartNo = models.CharField(max_length=255)
    # حوزه
    discipline = models.ForeignKey(DisciplineType, on_delete=models.CASCADE, related_name="product_discipline")
    # نوع تجهیزات اصلی
    equipmentType = models.ForeignKey(EquipmentType, on_delete=models.CASCADE, related_name="product_equipmentType")
    # شماره تجهیز
    equipmentTagNo = models.CharField(max_length=255)
    # عنوان مجتمع
    plant = models.ForeignKey(PlantType, on_delete=models.CASCADE, related_name="product_plant")
    # عنوان واحد فرایندی
    processUnit = models.ForeignKey(ProcessUnit, on_delete=models.CASCADE, related_name="product_processUnit")
    # سابقه ساخت داخل دارد 
    isManufactured = models.BooleanField(default=False)
    # شرکت سازنده داخلی
    manufactured = models.CharField(max_length=255,null=True,blank=True)
    # قیمت قطعه
    originalUnitPrice = models.DecimalField(default=0,max_digits=13,decimal_places=0)  
    # ارز
    currency = models.ForeignKey(CurrencyType, on_delete=models.PROTECT, related_name="product_currency")
    # نرخ تبدیل ارز در زمان ساخت داخل - ریال
    exchangeRate = models.IntegerField(null=True,blank=True)
    # تاریخ ساخت داخل
    ManufacturedData = models.DateTimeField(null=True,blank=True)
    #ساخته شده برای مجتمع 
    ManufacturedForPlant = models.ForeignKey(PlantType, on_delete=models.PROTECT, related_name="product_ManufacturedForPlant",null=True,blank=True)
    #صرفه جوییی ناشی از ساخت داخل 
    savingMony = models.FloatField(null=True,blank=True)
    # میزان رضایت
    Satisfaction = models.IntegerField(default=1,validators = [MinValueValidator(1),MaxValueValidator(5)])
    # end new item
    
    stock = models.PositiveIntegerField(default=0)
    status = models.IntegerField(choices=ProductStatusType.choices,default=ProductStatusType.draft.value)
    price = models.DecimalField(default=0,max_digits=10,decimal_places=0)
    discount_percent = models.IntegerField(default=0,validators = [MinValueValidator(0),MaxValueValidator(100)])
    
    avg_rate = models.FloatField(default=0.0)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-created_date"]
        
    def __str__(self):
        return self.title
    
    def get_price(self):        
        discount_amount = self.price * Decimal(self.discount_percent / 100)
        discounted_amount = self.price - discount_amount
        return round(discounted_amount)
    
    def is_discounted(self):
        return self.discount_percent != 0
    
    def is_published(self):
        return self.status == ProductStatusType.publish.value

    def save(self, *args, **kwargs):
        # چک کردن اینکه هر دو فیلد پر شده‌اند
        if self.originalUnitPrice and self.exchangeRate:
            # فرض کنید فیلد exchangeRate دارای فیلدی به نام rate باشد که مقدار نرخ تبدیل ارز را دارد
            self.savingMony = float(self.originalUnitPrice) * float(self.exchangeRate)
        else:
            self.savingMony = 0  # اگر فیلدها کامل نبودند، مقدار صرفه‌جویی صفر تنظیم شود
            
        super(ProductModel, self).save(*args, **kwargs)
    
class ProductImageModel(models.Model):
    product = models.ForeignKey(ProductModel,on_delete=models.CASCADE,related_name="product_images")
    file = models.ImageField(upload_to="product/extra-img/")
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-created_date"]

class ProductFileModel(models.Model):
    title = models.CharField(max_length=128)
    product = models.ForeignKey(ProductModel,on_delete=models.CASCADE,related_name="product_files")
    file = models.FileField(upload_to="product/files/")
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-created_date"]
        
class WishlistProductModel(models.Model):
    user = models.ForeignKey("accounts.User",on_delete=models.PROTECT)
    product = models.ForeignKey(ProductModel,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.product.title