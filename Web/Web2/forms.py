from importlib.metadata import files
from django import forms
from django.forms import ModelForm, fields, widgets
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import *
from django.forms.models import inlineformset_factory

class formLogin(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'type':'email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'type':'password'}))

class formRegistro(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Usuario
        fields = '__all__'
        exclude = ['last_login','usuario_activo','usuario_administrador']
        
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Las Contraseñas no coinciden')
        return cd['password2']
        
    def save(self,commit=True):
        user = super(formRegistro,self).save(commit=False)
        user.set_password(self.cleaned_data["password2"])
        if commit:
            user.save()
        return user