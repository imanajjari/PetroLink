from django import forms
from shop.models import ProductModel,ProductImageModel,ProductFileModel
class ProductForm(forms.ModelForm):
    ManufacturedData = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'form-control','type':'datetime-local'}))
    docData = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'form-control','type':'datetime-local'}))

    class Meta:
        model = ProductModel
        fields = [
            "category",
            "title",
            "slug",
            "image",
            "description",
            "brief_description",

            "mesc_code",
            "docNo",
            "docData",
            "doc_ver",
            "vendor",
            "manufacturerPartNo",
            "supplierPartNo",
            "discipline",
            "equipmentTagNo",
            "plant",
            "equipmentType",
            "processUnit",
            "isManufactured",
            "manufactured",
            "originalUnitPrice",
            "currency",
            "exchangeRate",
            "ManufacturedData",
            "ManufacturedForPlant",
            "savingMony",
            "Satisfaction",

            "stock",
            "status",
            "price",
            "discount_percent",
            

        ]

        error_messages = {
            'category': {'required': 'لطفا دسته‌بندی را انتخاب کنید.'},
            'title': {'required': 'لطفا عنوان محصول را وارد کنید.'},
            'slug': {'required': 'لطفا نامک (slug) را وارد کنید.'},
            'image': {'required': 'لطفا تصویر محصول را بارگذاری کنید.'},
            'description': {'required': 'لطفا توضیحات محصول را وارد کنید.'},
            'brief_description': {'required': 'لطفا توضیحات مختصر را وارد کنید.'},
            'mesc_code': {'required': 'لطفا کد MESC را وارد کنید.'},
            'docNo': {'required': 'لطفا شماره سند را وارد کنید.'},
            'docData': {'required': 'لطفا تاریخ سند را وارد کنید.'},
            'doc_ver': {'required': 'لطفا ورژن سند را وارد کنید.'},
            'vendor': {'required': 'لطفا نام تامین‌کننده را وارد کنید.'},
            'manufacturerPartNo': {'required': 'لطفا شماره قطعه سازنده را وارد کنید.'},
            'supplierPartNo': {'required': 'لطفا شماره قطعه تامین‌کننده را وارد کنید.'},
            'discipline': {'required': 'لطفا رشته را انتخاب کنید.'},
            'equipmentTagNo': {'required': 'لطفا شماره تگ تجهیزات را وارد کنید.'},
            'plant': {'required': 'لطفا کارخانه را انتخاب کنید.'},
            'equipmentType': {'required': 'لطفا نوع تجهیزات را انتخاب کنید.'},
            'processUnit': {'required': 'لطفا واحد فرآیندی را انتخاب کنید.'},
            'isManufactured': {'required': 'لطفا تعیین کنید که محصول تولید شده است یا خیر.'},
            'manufactured': {'required': 'لطفا مقدار ساخت را وارد کنید.'},
            'originalUnitPrice': {'required': 'لطفا قیمت واحد اولیه را وارد کنید.'},
            'currency': {'required': 'لطفا واحد ارزی را انتخاب کنید.'},
            'exchangeRate': {'required': 'لطفا نرخ ارز را وارد کنید.'},
            'ManufacturedData': {'required': 'لطفا تاریخ ساخت را وارد کنید.'},
            'ManufacturedForPlant': {'required': 'لطفا کارخانه مقصد را انتخاب کنید.'},
            'savingMony': {'required': 'لطفا مقدار صرفه‌جویی را وارد کنید.'},
            'Satisfaction': {'required': 'لطفا میزان رضایت را وارد کنید.'},
            'stock': {'required': 'لطفا موجودی انبار را وارد کنید.'},
            'status': {'required': 'لطفا وضعیت محصول را انتخاب کنید.'},
            'price': {'required': 'لطفا قیمت محصول را وارد کنید.'},
            'discount_percent': {'required': 'لطفا درصد تخفیف را وارد کنید.'},
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['slug'].widget.attrs['class'] = 'form-control'
        self.fields['category'].widget.attrs['class'] = 'form-control'
        self.fields['image'].widget.attrs['class'] = 'form-control'
        self.fields['brief_description'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['id'] = 'ckeditor'
        self.fields['stock'].widget.attrs['class'] = 'form-control'
        self.fields['stock'].widget.attrs['type'] = 'number'
        self.fields['status'].widget.attrs['class'] = 'form-select'
        self.fields['price'].widget.attrs['class'] = 'form-control'
        self.fields['discount_percent'].widget.attrs['class'] = 'form-control'

        self.fields['mesc_code'].widget.attrs['class'] = 'form-control'
        self.fields['docNo'].widget.attrs['class'] = 'form-control'
        self.fields['docData'].widget.attrs['class'] = 'form-control'
        self.fields['doc_ver'].widget.attrs['class'] = 'form-control'
        self.fields['vendor'].widget.attrs['class'] = 'form-control'
        self.fields['manufacturerPartNo'].widget.attrs['class'] = 'form-control'
        self.fields['supplierPartNo'].widget.attrs['class'] = 'form-control'
        self.fields['discipline'].widget.attrs['class'] = 'form-select'
        self.fields['equipmentType'].widget.attrs['class'] = 'form-select'
        self.fields['equipmentTagNo'].widget.attrs['class'] = 'form-control'
        self.fields['plant'].widget.attrs['class'] = 'form-select'
        self.fields['processUnit'].widget.attrs['class'] = 'form-select'
        self.fields['manufactured'].widget.attrs['class'] = 'form-control'
        self.fields['originalUnitPrice'].widget.attrs['class'] = 'form-control'
        self.fields['currency'].widget.attrs['class'] = 'form-select'
        self.fields['exchangeRate'].widget.attrs['class'] = 'form-select'
        self.fields['ManufacturedData'].widget.attrs['class'] = 'form-control'
        self.fields['ManufacturedForPlant'].widget.attrs['class'] = 'form-select'
        self.fields['savingMony'].widget.attrs['class'] = 'form-control'
        self.fields['Satisfaction'].widget.attrs['class'] = 'form-control'



class ProductImageForm(forms.ModelForm):


    class Meta:
        model = ProductImageModel
        fields = [
            "file",
        ]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['file'].widget.attrs['class'] = 'form-control'
        self.fields['file'].widget.attrs['accept'] = 'image/png, image/jpg, image/jpeg'

class ProductFileForm(forms.ModelForm):
    

    class Meta:
        model = ProductFileModel
        fields = [
            "title",
            "file",
        ]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['file'].widget.attrs['class'] = 'form-control'
        # self.fields['file'].widget.attrs['accept'] = 'image/png, image/jpg, image/jpeg'
