from django import forms
from django.core.exceptions import ValidationError

from app1.models import Category, Size


class CategoryAddForm(forms.Form):
    name = forms.CharField(max_length=64)

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')

        if name == '':
            raise forms.ValidationError('Brak kategorii!')

class SizeAddForm(forms.Form):
    name = forms.CharField(max_length=64)

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')

        if name == '':
            raise forms.ValidationError('Brak rozmiaru!')

class ProductAddForm(forms.Form):
    name = forms.CharField(max_length=64)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField(max_digits=5, decimal_places=2)
    current_quantity = forms.IntegerField()
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    size = forms.ModelChoiceField(queryset=Size.objects.all())


    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')

        if name == '':
            raise forms.ValidationError('Brak towaru!')
