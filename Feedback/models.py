from django.db import models
from django.core.exceptions import ValidationError
from django.core import validators
import re


TITLE_CHOICES = {
	('....','....'),
	('Mr','Mr'),
	('Mrs' , 'Mrs'),
	('Ms','Ms'),
}
def validate_name(value,length=5):
	regex = r"([a-zA-Z]+)"
	if not re.search(regex,value) or len(str(value)) < length:
		raise ValidationError(u"%r is Not a Valid Name"%value)

def validate_len(value,length=20):
	regex = r"([a-zA-Z]+)"
	if not re.search(regex,value) or len(str(value)) < length:
		raise ValidationError(u"Not Valid Be More Specific")

class NameManager(models.Manager):
	def get_queryset(self,**kwargs):
		return super(NameManager,self).get_queryset(**kwargs).count()
		
class Feedback(models.Model):
	Name   = models.CharField(validators=[validate_name],max_length = 100)
	Title = models.CharField(max_length=3)
	Subject = models.CharField(validators=[validate_name],max_length = 100)
	Message = models.CharField(validators=[validate_len],max_length = 1002)	
	count = NameManager()	
