from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


class UserManager(BaseUserManager):
  def create_user(self, user_id, nickname, password):
    if not user_id:
      raise ValueError('Please enter your ID')

    user = self.model(
      user_id=user_id,
      nickname=nickname,
    )

    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self, user_id, nickname, password):
    user = self.create_user(
      user_id=user_id,
      nickname=nickname,
      password=password,
    )
    user.is_admin = True
    user.save(using=self._db)
    return user

class User(AbstractBaseUser):
  user_id = models.CharField(max_length=50, primary_key=True)
  nickname = models.CharField(max_length=50, unique=True)
  is_active = models.BooleanField(default=True)
  is_admin = models.BooleanField(default=False)

  objects = UserManager()

  USERNAME_FIELD = 'user_id'
  REQUIRED_FIELDS = ['nickname']

  def __str__(self):
    return self.nickname

  def has_perm(self, perm, obj=None):
    return True

  def has_module_perms(self, app_label):
    return True

  @property
  def is_staff(self):
    return self.is_admin