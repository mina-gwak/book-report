from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from account.forms import LoginForm, MyLoginView

urlpatterns = [
    path('', MyLoginView.as_view(authentication_form=LoginForm), name='login'),
    path('register/', views.register, name='register'),
    path('', LogoutView.as_view(), name='logout'),
]