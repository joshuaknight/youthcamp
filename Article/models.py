from django.db import models 
from django.core import validators 
from django.core.exceptions import ValidationError
import re 


def author_article(self):
		return "%s %s"%(self.author_name,self.article_name)
link_name = property(author_article)

def valid_name(value,length=5):
	regex = r"([a-zA-Z]+)"
	if not re.search(regex,value) or len(str(value)) < length:
		raise ValidationError("Not a Valid Name")

def valid_content(value,length=20):
	regex = r"([a-zA-Z]+)"
	stuff = value.split(' ')
	if not re.search(regex,value) or len(stuff) < length:
		raise ValidationError("Not Valid Be More Specific")

class AuthorManager(models.Manager):
	def get_queryset(self):
		return super(AuthorManager,self).get_queryset().count()

class New_Article(models.Model):
	author_name = models.CharField(max_length = 10,validators = [valid_name]) 
	article_name = models.CharField(max_length=30,validators=[valid_name])	
	content = models.CharField(max_length=20000,validators=[valid_content])
	publ_date = models.DateField(verbose_name = "Publication Date")
	author = AuthorManager()	

		