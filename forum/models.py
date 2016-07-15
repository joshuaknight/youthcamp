from django.db import models
from django.contrib.auth.models import Permission,Group 
from django.core.exceptions import ValidationError
from django.core import validators
import re

class Login(models.Model):
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=20)	
