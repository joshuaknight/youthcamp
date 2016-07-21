from django.forms import ModelForm,Textarea
from django import forms
from bootstrap3_datetime.widgets import DateTimePicker
from Article.models import New_Article
from django.utils import timezone

class MyArticle(ModelForm):
	class Meta:
		model = New_Article
		fields = '__all__'

		widgets = {
			'content' : Textarea(attrs = {'cols':50,'rows':10}),
			'publ_date' : DateTimePicker(options={"format": "YYYY-MM-DD",
																"pickTime": False})
			}

		inital = {
			'publ_date' : timezone.now()
		}			

		
