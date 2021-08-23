from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
# Register your models here.

# set password in admin panel read-only
class AccountAdmin(UserAdmin):
    list_display = ('email', 'firstName', 'lastName', 'username', 'last_login', 'is_active' , 'date_joined')
    list_display_links = ('email', 'firstName', 'lastName')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('date_joined',)

    # Mandatory by django. Reference: https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#a-full-example
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)

