from django import forms
from django.forms import ModelForm, fields, widgets
from .models import *

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        exclude = ['id_usuario']
        widgets={
            'myfield':forms.TextInput(attrs={'class':'texto_input'})
        }