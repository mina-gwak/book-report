from django.db import models

# Create your models here.
class Account(models.Model):
  name = models.CharField(max_length = 50)
  userId = models.CharField(max_length = 50)
  userPw = models.CharField(max_length = 50)