from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from account.forms import LoginForm
urlpatterns = [
    path('', LoginView.as_view(authentication_form=LoginForm), name='login'),
    path('register/', views.register, name='register'),
    path('main/', views.main, name='main'),
]