from django import forms
from .models import Image

class MyModelForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']
