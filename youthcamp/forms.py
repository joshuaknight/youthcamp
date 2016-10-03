from django.forms import ModelForm
#from .models import Login
from django import forms

class MyLogin(ModelForm):
	class Meta:
		model = Login
		fields = '__all__'

class MySignup(ModelForm):
	class Meta:
		model = Login
		fields = '__all__'		