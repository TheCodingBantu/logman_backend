from django.contrib import admin
from .models import LogmanUser


# Register your models here.

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import LogmanUser

class LogmanUserAdmin(BaseUserAdmin):
    model = LogmanUser
    list_display = ('email', 'name', 'is_staff', 'is_active', 'organization')
    list_filter = ('is_staff', 'is_active', 'organization')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'organization')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', 'is_staff', 'is_active', 'organization')}
        ),
    )
    search_fields = ('email', 'name')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)

admin.site.register(LogmanUser, LogmanUserAdmin)
