from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from accounts.models import User


class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2')}
         ),
    )
    list_display = ('username', 'last_name', 'email', 'country')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'country', 'birthday')}),
        ('Permissions', {'fields': ('is_superuser', 'is_staff')}),
    )

admin.site.register(User, CustomUserAdmin)
