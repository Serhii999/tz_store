from django.forms import ModelForm
from .models import *
from django import forms


class TzUserForm(ModelForm):
    confirm_pass = forms.CharField(max_length=100)

    class Meta:
        model = StoreUser
        fields = ('username', 'password', 'confirm_pass')

    def clean(self):
        clean_data = super().clean()
        if clean_data.get('password') != clean_data.get('confirm_pass'):
            raise forms.ValidationError('Passwords are not equal!')


class CategoryCreateForm(ModelForm):
    class Meta:
        model = Categories
        fields = ('title', 'description', 'picture')


class ProductCreateForm(ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'image', 'price', 'quantity', 'description')


class OrderCreateForm(ModelForm):
    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$')

    class Meta:
        model = Order
        fields = ('name', 'surname', 'email', 'phone_number')
