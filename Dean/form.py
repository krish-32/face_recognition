from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *


class user(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'input'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'input'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'input'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']
class add_staff(forms.ModelForm):
    class Meta:
        model=staff_data
        fields='__all__'
        widgets={
            'Select':forms.Select(attrs={'class':'input','id':'dept'}),
            'name':forms.TextInput(attrs={'class':'input'}),
            'position':forms.TextInput(attrs={'class':'input'}),
            'staff_id':forms.NumberInput(attrs={'class':'input'}),
            'email':forms.EmailInput(attrs={'class':'input'}),
            'phone':forms.NumberInput(attrs={'class':'input'}),
            'department':forms.TextInput(attrs={'class':'input'}),
            'degree':forms.TextInput(attrs={'class':'input'}),
            'linkedin':forms.TextInput(attrs={'class':'input'}),
            'github':forms.TextInput(attrs={'class':'input'}),
            'whatsapp':forms.TextInput(attrs={'class':'input'}),
            'photo':forms.FileInput(attrs={'class':'input','id':'photo'}),
        }

class add_hod(forms.ModelForm):
    class Meta:
        model=hod
        fields='__all__'
        widgets={
            
            'name':forms.TextInput(attrs={'class':'input'}),
            'position':forms.TextInput(attrs={'class':'input'}),
            'staff_id':forms.NumberInput(attrs={'class':'input'}),
            'email':forms.EmailInput(attrs={'class':'input'}),
            'phone':forms.NumberInput(attrs={'class':'input'}),
            'department':forms.TextInput(attrs={'class':'input'}),
            'degree':forms.TextInput(attrs={'class':'input'}),
            'linkedin':forms.TextInput(attrs={'class':'input'}),
            'github':forms.TextInput(attrs={'class':'input'}),
            'whatsapp':forms.TextInput(attrs={'class':'input'}),
            'photo':forms.FileInput(attrs={'class':'input','id':'photo'}),
        }
class register(forms.ModelForm):
    class Meta:
        model=staff_register
        fields='__all__'
        widgets={
            'email':forms.EmailInput(attrs={'class':'input'}),
            'staff_id':forms.NumberInput(attrs={'class':'input'}),
            'name':forms.TextInput(attrs={'class':'input'}),
            'username':forms.TextInput(attrs={'class':'input'}),
            'password':forms.PasswordInput(attrs={'class':'input'}),
            'confirm_pass':forms.PasswordInput(attrs={'class':'input'}),
        }