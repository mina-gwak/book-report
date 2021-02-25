from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main, name='main'),
    path('search/', views.search, name='search'),
    path('add-book/', views.addBook, name='addBook'),
    path('save-record/', views.saveRecord, name='saveRecord'),
    path('my-record/<str:book_id>/', views.myRecord, name='myRecord'),
    path('update-record/', views.updateRecord, name='updateRecord'),
    path('delete-record/<str:book_id>/', views.delRecord, name='delRecord'),
]