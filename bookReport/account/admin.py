from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import User

# Register your models here.
class UserAdmin(BaseUserAdmin):
  form = UserChangeForm
  add_form = UserCreationForm

  list_display = ('user_id', 'nickname', 'is_admin')
  list_filter = ('is_admin',)
  fieldsets = (
    (None, {'fields': ('user_id', 'password')}),
    ('Personal info', {'fields': ('nickname',)}),
    ('Permissions', {'fields': ('is_admin',)}),
  )

  add_fieldsets = (
    (None, {
      'classes': ('wide',),
      'fields': ('user_id', 'nickname', 'password')}
    ),
  )
  search_fields = ('user_id',)
  ordering = ('user_id',)
  filter_horizontal = ()

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)