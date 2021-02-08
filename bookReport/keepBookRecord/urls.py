from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main, name='main'),
    path('search/', views.search, name='search'),
    path('add-book/', views.addBook, name='addBook'),
]