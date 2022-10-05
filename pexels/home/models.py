from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
 username = models.ForeignKey(User, on_delete=models.CASCADE)
 password = models.CharField(max_length=200)

class File(models.Model):
  file = models.FileField(blank=False, null=False)
  timestamp = models.DateTimeField(auto_now_add=True)