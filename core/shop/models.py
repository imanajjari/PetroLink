from django.db import models
from decimal import Decimal
from django.core.validators import MaxValueValidator, MinValueValidator


class ProductStatusType(models.IntegerChoices):
    publish = 1 ,("نمایش")
    draft = 2 ,("عدم نمایش")


class DisciplineType(models.IntegerChoices):
    Mechanics = 1 ,("مکانیک")
    rotatingMachines = 2 ,("ماشین آلات دوار")
    precisionTools = 3 ,("ابزار دقیق")
    electricity = 4 ,("برق")
    misc = 5 ,("متفرقه")

class EquipmentType(models.IntegerChoices):
    pump = 1 ,("پمپ")
    compressor = 2 ,("کمپرسور")
    exchenger = 3 ,("مبدل")
    tower = 4 ,("برج")
    tank = 5 ,("تانک")
    drum = 6 ,("طبل")
    special = 7 ,("خاص")
    equipment = 8 ,("تجهیزات")
    other = 9 ,("دیگر")

class PlantType(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode=True,unique=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-created_date"]
        
    def __str__(self):
        return self.name

class ProcessUnit(models.IntegerChoices):
    ammonia = 1 ,("آمونیاک")
    urea = 2 ,("اوره")
    industrialWater = 3 ,("آب صنعتی")

class CurrencyType(models.IntegerChoices):
    dollar = 1 ,("دلار")
    euro = 2 ,("یورو")
    Dirham = 3 ,("درهم")
    yuan = 4 ,("یوان")


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
    # شماره مدرک
    docNo = models.CharField(max_length=255,null=True,blank=True)
    # سازنده اصلی
    vendor = models.CharField(max_length=255,null=True,blank=True)
    # شماره قطعه کارخانه اصلی سازنده
    manufacturerPartNo = models.CharField(max_length=255,null=True,blank=True)
    # شماره قطعه سازنده
    supplierPartNo = models.CharField(max_length=255,null=True,blank=True)
    # حوزه
    discipline = models.IntegerField(choices=DisciplineType.choices,default=DisciplineType.misc.value)
    # نوع تجهیزات اصلی
    equipmentType = models.IntegerField(choices=EquipmentType.choices,default=EquipmentType.other.value)
    # شماره تجهیز
    equipmentTagNo = models.CharField(max_length=255,null=True,blank=True)
    # عنوان مجتمع
    plant = models.ForeignKey(PlantType, on_delete=models.CASCADE, related_name="product_plant")
    # عنوان واحد فرایندی
    processUnit = models.IntegerField(choices=ProcessUnit.choices,default=ProcessUnit.ammonia.value)
    # توضیحات
    remark = models.TextField(null=True,blank=True)
    # سابقه ساخت داخل دارد 
    isManufactured = models.BooleanField(default=False)
    # شرکت سازنده داخلی
    manufactured = models.CharField(max_length=255,null=True,blank=True)
    # قیمت قطعه
    originalUnitPrice = models.DecimalField(default=0,max_digits=10,decimal_places=0)  
    # ارز
    currency = models.IntegerField(choices=CurrencyType.choices,default=CurrencyType.dollar.value)
    # نرخ تبدیل ارز در زمان ساخت داخل - ریال
    exchangeRate = models.IntegerField(choices=CurrencyType.choices,default=CurrencyType.dollar.value)
    # تاریخ ساخت داخل
    ManufacturedData = models.DateTimeField(null=True,blank=True)
    #ساخته شده برای مجتمع 
    ManufacturedForPlant = models.ForeignKey(PlantType, on_delete=models.CASCADE, related_name="product_ManufacturedForPlant")
    #صرفه جوییی ناشی از ساخت داخل 
    savingMony = models.FloatField(null=True,blank=True)
    # میزان رضایت
    Satisfaction = models.IntegerField(default=0,validators = [MinValueValidator(0),MaxValueValidator(5)])
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
    
class ProductImageModel(models.Model):
    product = models.ForeignKey(ProductModel,on_delete=models.CASCADE,related_name="product_images")
    file = models.ImageField(upload_to="product/extra-img/")
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-created_date"]

class ProductFileModel(models.Model):
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