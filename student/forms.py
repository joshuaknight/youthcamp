from django.forms import ModelForm,Textarea
from student.models import *
from django import forms
import re 
from django.forms.extras.widgets import SelectDateWidget
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from bootstrap3_datetime.widgets import DateTimePicker

import datetime

class RegistrationForm(ModelForm):
	class Meta:
		model = Registration
		fields = '__all__'		
		localized_fields = '__all__'

		widgets = {
					#'faith_home' : forms.Select(choices = FAITH_CHOICE),
					'gender'	 : forms.Select(choices=GENDER_CHOICE),				 	
					'date_of_birth': DateTimePicker(options={"format": "YYYY-MM-DD",
				
                                       "pickTime": False})
					}
		help_texts = {
					'first_name'	: _('eg:\'joshua\''),
					'last_name':_("eg:'knight'"),					
					'date_of_birth' : _('eg:\'YYYY-MM-DAY\''),
					'faith_home'	: _('eg:location')
		
					}

		error_messages = {
				'required': 'Need a Valid Image', 
				'invalid': 'Email is invalid'
				}						
		

	def clean_date_of_birth(self):
		today = datetime.datetime.today()
		date = '%d-%d-%d'%(today.year,today.month,today.day)
		date_of_birth = self.cleaned_data['date_of_birth']
		if date_of_birth.year > today.year-14 or date_of_birth.year >= today.year:
			raise ValidationError('You Must Be Utleast 14Years Old')			
		else:			
			return self.cleaned_data['date_of_birth']			



      		
