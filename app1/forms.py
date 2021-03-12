from django import forms
from django.core.exceptions import ValidationError

from app1.models import Category, Size, Brand, Color


class CategoryAddForm(forms.Form):

    name = forms.CharField(max_length=64)
    kod = forms.CharField(max_length=5)

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')

        if name == '':
            raise forms.ValidationError('Brak kategorii!')

class SizeAddForm(forms.Form):
    KOD_LENGTH = 2
    name = forms.CharField(max_length=64)
    kod = forms.CharField(max_length=5)

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        kod = cleaned_data.get('kod')


        if name == '':
            raise forms.ValidationError('Brak rozmiaru!')

        if len(kod) != self.KOD_LENGTH:
            raise forms.ValidationError(f'Kod ma mieć {self.KOD_LENGTH} znaki!')

class BrandAddForm(forms.Form):
    KOD_LENGTH = 2
    name = forms.CharField(max_length=64)
    kod = forms.CharField(max_length=5)

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        kod = cleaned_data.get('kod')

        # breakpoint()
        if name == '':
            raise forms.ValidationError('Brak brandu!')

        if len(kod) != self.KOD_LENGTH:
            raise forms.ValidationError(f'Kod ma {self.KOD_LENGTH} znaki!')

class ColorAddForm(forms.Form):
    KOD_LENGTH = 1
    name = forms.CharField(max_length=64)
    kod = forms.CharField(max_length=5)

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        kod = cleaned_data.get('kod')

        # breakpoint()
        if name == '':
            raise forms.ValidationError('Brak koloru!')

        if len(kod) != self.KOD_LENGTH:
            raise forms.ValidationError(f'Kod ma {self.KOD_LENGTH} znaki!')

class ProductAddForm(forms.Form):
    name = forms.CharField(max_length=64)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField(max_digits=5, decimal_places=2)
    current_quantity = forms.IntegerField()
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    size = forms.ModelChoiceField(queryset=Size.objects.all())
    brand = forms.ModelChoiceField(queryset=Brand.objects.all())
    color = forms.ModelChoiceField(queryset=Color.objects.all())


    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')

        if name == '':
            raise forms.ValidationError('Brak towaru!')
