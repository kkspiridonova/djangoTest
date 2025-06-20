from django import forms
from .models import Clothrs

class ClothrsForm(forms.ModelForm):
    class Meta:
        model = Clothrs
        fields = ['name','description','price','size','colour','photo','is_exist','category','collection']