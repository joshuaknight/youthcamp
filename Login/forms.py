from django.forms import ModelForm
from .models import Login
from django import forms 
from django.core.exceptions import ValidationError
from django.core import validators


class Mylogin(ModelForm):
	class Meta:
		model = Login
		fields = '__all__'
		
		labels ={
		  'username' : 'username',
		  'password' : 'password',
		}
		widgets= {
			'password' : forms.PasswordInput
			}