from importlib.metadata import files
from django import forms
from django.forms import ModelForm, fields, widgets
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import *
from django.forms.models import inlineformset_factory

class formRegistro(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        exclude = ['last_login','usuario_activo','usuario_administrador']