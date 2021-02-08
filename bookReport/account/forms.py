from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import ReadOnlyPasswordHashField, AuthenticationForm, UsernameField
from django.core.exceptions import ValidationError


from .models import User


class UserCreationForm(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput, label='password')

  def __init__(self, *args, **kwargs):
    super().__init__(*args,**kwargs)
    self.fields['user_id'].label = 'id'
    self.fields['nickname'].label = 'nickname'
    self.label_suffix = None

  class Meta:
    model = User
    fields = ('user_id', 'nickname')

  def clean_user_id(self):
    user_id = self.cleaned_data.get('user_id')

    if User.objects.filter(user_id=user_id).exists():
      raise forms.ValidationError('This ID is already in use.')
    return user_id

  def clean_nickname(self):
    nickname = self.cleaned_data.get('nickname')

    if User.objects.filter(nickname=nickname).exists():
      raise forms.ValidationError('This nickname is already in use.')
    return nickname
  
  def save(self, commit=True):
    user = super().save(commit=False)
    user.set_password(self.cleaned_data["password"])
    if commit:
      user.save()
    return user


class UserChangeForm(forms.ModelForm):
  password = ReadOnlyPasswordHashField()

  class Meta:
    model = User
    fields = ('user_id', 'nickname', 'password', 'is_active', 'is_admin')

  def clean_password(self):
    return self.initial["password"]

class LoginForm(forms.Form):

  user_id = UsernameField(widget=forms.TextInput(attrs={
    'autofocus': True, 
    'placeholder': 'ID',
    'class': 'user-id'}))
  password = forms.CharField(
      strip=False,
      widget=forms.PasswordInput(attrs={
        'autocomplete': 'current-password', 
        'placeholder': 'Password',
        'class': 'user-password'
        })
  )

  error_messages = {
    'invalid_login': (
      "Please enter a correct id and password. Note that both "
      "fields may be case-sensitive."
    ),
    'inactive': "This account is inactive.",
  }

  def __init__(self, request=None, *args, **kwargs):
    self.request = request
    self.user_cache = None
    super().__init__(*args, **kwargs)

    # Set the max length and label for the "username" field.
    self.username_field = User._meta.get_field(User.USERNAME_FIELD)
    username_max_length = self.username_field.max_length or 254
    self.fields['user_id'].max_length = username_max_length
    self.fields['user_id'].widget.attrs['maxlength'] = username_max_length
    self.fields['user_id'].label = ''
    self.fields['password'].label = ''

  def clean(self):
    user_id = self.cleaned_data.get('user_id')
    password = self.cleaned_data.get('password')

    if user_id is not None and password:
      self.user_cache = authenticate(self.request, user_id=user_id, password=password)
      if self.user_cache is None:
        raise self.get_invalid_login_error()
      else:
        self.confirm_login_allowed(self.user_cache)

    return self.cleaned_data

  def confirm_login_allowed(self, user):
    if not user.is_active:
      raise ValidationError(
        self.error_messages['inactive'],
        code='inactive',
        )

  def get_user(self):
    return self.user_cache

  def get_invalid_login_error(self):
    return ValidationError(
      self.error_messages['invalid_login'],
      code='invalid_login',
      params={'user_id': self.username_field.verbose_name},
    )