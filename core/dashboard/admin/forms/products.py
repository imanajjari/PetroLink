from django import forms
from shop.models import ProductModel,ProductImageModel,ProductFileModel
class ProductForm(forms.ModelForm):
    ManufacturedData = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'form-control','type':'datetime-local'}))

    class Meta:
        model = ProductModel
        fields = [
            "category",
            "title",
            "slug",
            "image",
            "description",
            "brief_description",
            "stock",
            "status",
            "price",
            "discount_percent",
            
            "docNo",
            "vendor",
            "manufacturerPartNo",
            "supplierPartNo",
            "discipline",
            "equipmentType",
            "equipmentTagNo",
            "plant",
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

        ]
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

        self.fields['docNo'].widget.attrs['class'] = 'form-control'
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