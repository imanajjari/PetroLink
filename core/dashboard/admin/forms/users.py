from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm


User = get_user_model()
class UserForm(forms.ModelForm):
    class Meta:
        model = User
    
        fields = [
            "email",
            "is_active",
            "is_verified",
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add custom classes to fields
        self.fields['email'].widget.attrs['class'] = 'form-control mx-3 Disabled text-center mb-3'
        
        self.fields['is_active'].widget.attrs['class'] = 'form-check-input mb-3'
        self.fields['is_verified'].widget.attrs['class'] = 'form-check-input mb-3'

class AdminChangePasswordUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["password",]
        widgets = {
            'password': forms.PasswordInput()
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['password'].widget.attrs['class'] = 'form-control text-center'
            self.fields['password'].widget.attrs['placeholder'] = "پسورد را وارد نمایید"

class AdminUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'is_active', 'is_verified']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_active'] = forms.BooleanField(initial=True, widget=forms.HiddenInput())
        self.fields['is_verified'] = forms.BooleanField(initial=True, widget=forms.HiddenInput())

        # Add custom classes to fields
        self.fields['email'].widget.attrs['class'] = 'form-control mx-3 Disabled text-center mb-3'
        
        self.fields['password1'].widget.attrs['class'] = 'form-control mx-3 Disabled text-center mb-3'
        self.fields['password2'].widget.attrs['class'] = 'form-control mx-3 Disabled text-center mb-3'

class SuperUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'type', 'is_active', 'is_verified']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_active'] = forms.BooleanField(initial=True, widget=forms.HiddenInput())
        self.fields['is_verified'] = forms.BooleanField(initial=True, widget=forms.HiddenInput())

        # Add custom classes to fields
        self.fields['type'].choices = [(1, 'کاربر ساده'), (2, 'ادمین')]
        self.fields['email'].widget.attrs['class'] = 'form-control mx-3 Disabled text-center mb-3'
        
        self.fields['password1'].widget.attrs['class'] = 'form-control mx-3 Disabled text-center mb-3'
        self.fields['password2'].widget.attrs['class'] = 'form-control mx-3 Disabled text-center mb-3'
        self.fields['type'].widget.attrs['class'] = 'form-select mx-3'

        
        