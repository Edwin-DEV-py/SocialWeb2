from importlib.metadata import files
from django import forms
from django.forms import ModelForm, fields, widgets
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import *
from django.contrib.auth import authenticate
from django.forms.models import inlineformset_factory

class registro(UserCreationForm):
    username = forms.EmailField(label="Email",widget=forms.EmailInput)
    class Meta:
        model = User
        fields = ['first_name','last_name','username','password1','password2']
        help_texts = {k:"" for k in fields}
        
class UniversitarioForm(ModelForm):
    class Meta:
        model = universitario
        fields = '__all__'
        exclude = ['user','lider']
        
class UniversitarioForm2(ModelForm):
    class Meta:
        model = universitario
        fields = '__all__'
        exclude = ['user']
        
        
class grupoForm(ModelForm):
    class Meta:
        model=grupo
        fields = '__all__'
        exclude = ['user']

class propuestaForm(ModelForm):
    class Meta:
        model=propuesta
        fields = '__all__'
        exclude = ['user']
        
    widgets ={
            'myfield':forms.TextInput(attrs={'class':'form-control'})
        }

class contacto_form(ModelForm):
    class Meta:
        model=contacto
        fields = '__all__'
        exclude = ['user']