from django import forms
from django.forms import ModelForm, TextInput, DateInput, Select, SelectDateWidget, HiddenInput, PasswordInput, EmailInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm



class UserCreate(UserCreationForm):
    #email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control','required': True}),
            'username': TextInput(attrs={'class': 'form-control'}),
            'password1': PasswordInput(attrs={'class': 'form-control'}),
            'password2': PasswordInput(attrs={'class': 'form-control'})
            
        }
        error_messages = {
            'first_name': {
                'required': 'Este campo é obrigatório'
            },
            'last_name': {
                'required': 'Este campo é obrigatório'
            },
            'email': {
                'required': 'Este campo é obrigatório'
            },
            'username': {
                'required': 'Este campo é obrigatório'
            },
            'password1': {
                'required': 'Este campo é obrigatório'
            },
            'password2': {
                'required': 'Este campo é obrigatório'
            },
            
        }

    def save(self, commit=True):
        user = super(UserCreate, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        #user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class UpdateUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','password']
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control','required': True}),
            'username': TextInput(attrs={'class': 'form-control'}),            
        }