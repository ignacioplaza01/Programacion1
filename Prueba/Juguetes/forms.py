from django import forms
from Juguetes.models import Juguetes

class RegistroJuguete(forms.ModelForm):
    class Meta:
        model = Juguetes
        fields = '__all__'
        marca = forms.CharField()
        categoria = forms.CharField()
        producto = forms.CharField()
        edad = forms.CharField(required=False)
        precio = forms.CharField()
        cantidad = forms.CharField()
         