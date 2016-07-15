from django import forms 
import re
from django.utils.translation import ugettext_lazy as _
from .models import *
from django.forms import ModelForm,Textarea,CharField

class ContactForm(ModelForm):
	class Meta:
		model = Feedback
		fields = ('Title','Name','Subject','Message')
		widgets = {
			'Message' : Textarea(attrs={'cols' : 50,'rows' : 10}),
			'Title':forms.Select(choices = TITLE_CHOICES),
		}

		help_texts = {
			'Message' : _('Enter a valid Message'),	
			'Name' : _("Enter a Name"),
			'Title' : _("Select a Proper Title "),
			'Subject' :_("Tell Me What is the theme of your Feedback"),
		}
	
	
	def clean_Feedback(self):
		message = self.cleaned_data['Feedback']
		splitted = message.split(' ')
		num_data = len(splitted)
		if(num_data <= 4):
			raise forms.ValidationError('Please Enter a Valid Message')
		return message 

	
