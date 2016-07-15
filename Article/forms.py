from django.forms import ModelForm,Textarea
from django import forms
from django.contrib.admin.widgets import AdminDateWidget as date
from Article.models import New_Article

class MyArticle(ModelForm):
	class Meta:
		model = New_Article
		fields = '__all__'

		widgets = {
			'content' : Textarea(attrs = {'cols':50,'rows':10}),
			'publ_date' : date
		}
