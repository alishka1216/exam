from django import forms
from django.core.validators import MinValueValidator


class BookForm(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    mail = forms.EmailField(max_length=100, required=False)
    description = forms.CharField(max_length=3000, required=True, widget=forms.Textarea)
