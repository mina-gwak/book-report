from django.db import models
from account.models import User
import uuid
from datetime import date

# Create your models here.
class Book(models.Model):

  id = models.UUIDField(primary_key=True, default=uuid.uuid4)
  title = models.CharField(max_length=300)
  author = models.CharField(max_length=300)
  pubdate = models.CharField(max_length=50)
  publisher = models.CharField(max_length=100)
  image = models.CharField(max_length=1000)
  user = models.ManyToManyField(User, through='Record')

  def __str__(self):
    return self.title

class Record(models.Model):

  now_reading = models.CharField(max_length=50)
  start_date = models.DateField()
  end_date = models.DateField(null=True, blank=True)
  impression = models.TextField()
  rating = models.CharField(max_length=50)
  user = models.ForeignKey(User, to_field='nickname', on_delete=models.CASCADE)
  book = models.ForeignKey(Book, on_delete=models.CASCADE)

class Quotes(models.Model):

  content = models.TextField()
  page = models.CharField(max_length=50)
  date = models.DateField()
  record = models.ForeignKey(Record, on_delete=models.CASCADE)