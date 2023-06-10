from django import forms
from .models import *

INPUT_STYLE='w-full py-3 px-4 rounded-xl'

class AddItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields=('name','price','description','category','image')
        widgets = {
            'name':forms.TextInput(attrs={'class':INPUT_STYLE}),
            'category':forms.Select(attrs={'class':INPUT_STYLE}),
            'price':forms.NumberInput(attrs={'class':INPUT_STYLE}),
            'description':forms.Textarea(attrs={'class':INPUT_STYLE}),
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields=('name','price','description','is_sold','image')
        widgets = {
            'name':forms.TextInput(attrs={'class':INPUT_STYLE}),
            'price':forms.NumberInput(attrs={'class':INPUT_STYLE}),
            'description':forms.Textarea(attrs={'class':INPUT_STYLE}),
        }