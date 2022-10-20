from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
 username = models.ForeignKey(User, on_delete=models.CASCADE)
 password = models.CharField(max_length=200)

class File(models.Model):
  file = models.FileField(blank=False, null=False)
  timestamp = models.DateTimeField(auto_now_add=True)
  

# model named Post
class Post(models.Model):
	Male = 'M'
	FeMale = 'F'
	GENDER_CHOICES = (
	(Male, 'Male'),
	(FeMale, 'Female'),
	)

	# define a username filed with bound max length it can have
	username = models.CharField( max_length = 20, blank = False,
								null = False)
	
	# This is used to write a post
	text = models.TextField(blank = False, null = False)
	
	# Values for gender are restricted by giving choices
	gender = models.CharField(max_length = 6, choices = GENDER_CHOICES,
							default = Male)
	
	time = models.DateTimeField(auto_now_add = True)
