from django.forms import ModelForm,Textarea
from student.models import *
from django import forms
import re 
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin.widgets import AdminDateWidget

class RegisForm(ModelForm):
	class Meta:
		model = Registration
		fields = '__all__'
		localized_fields = '__all__'

		widgets = {
					'faith_home' : forms.Select(choices = FAITH_CHOICE),
					'gender'	 : forms.Select(choices=GENDER_CHOICE),
				 	'annual_income':forms.Select(choices=Annual_Choice),
					'date_of_birth' : AdminDateWidget
					}
		help_texts = {
					'first_name'	: _('eg:\'joshua\''),
					'last_name':_("eg:'knight'"),
					'annual_income':('eg:12 * monthly salary'),
					'date_of_birth' : _('eg:\'YYYY-MM-DAY\''),
					'faith_home'	: _('eg:location')
					}	
	


      		
