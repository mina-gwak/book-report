from django.shortcuts import render, get_object_or_404, redirect
# from .models import Account
from django import forms
from account.forms import UserCreationForm,AuthenticationForm

# Create your views here.
def login(request):
  return render(request, 'login.html', {'form': login_form})

def register(request):
  regi_form = UserCreationForm()
  if request.method == 'POST':
    filled_form = UserCreationForm(request.POST)
    if filled_form.is_valid():
      filled_form.save()
      return redirect('login')
    else:
      return render(request, 'register.html',{
      'regi_form': filled_form,
      })
  return render(request, 'register.html', {'regi_form': regi_form})