from django.contrib import admin
from .models import Book, Quotes, Record

# Register your models here.
admin.site.register(Book)
admin.site.register(Quotes)
admin.site.register(Record)