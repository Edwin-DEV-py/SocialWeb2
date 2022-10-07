from importlib.metadata import files
from django import forms
from django.forms import ModelForm, fields, widgets
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import *
from django.forms.models import inlineformset_factory

class formLogin(forms.Form):
    class Meta:
        model = Usuario
        fields = '__all__'
        exclude = ['last_login','usuario_activo','usuario_administrador']

class formRegistro(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Usuario
        fields = '__all__'
        exclude = ['last_login','usuario_activo','usuario_administrador']
        
    def save(self,commit=True):
        user = super(formRegistro,self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user