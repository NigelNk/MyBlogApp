from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .forms import UserAccountChangeForm, UserAccountCreationForm
from users.models import UserAccount, UserProfile


@admin.register(UserAccount)
class UserAccountAdmin(UserAdmin):
    add_form = UserAccountCreationForm
    form = UserAccountChangeForm
    model = UserAccount

    list_display = ['email', 'username','is_active', 'is_staff', 'is_superuser']
    list_filter = ['is_staff',]

    search_fields = ['email', 'username']

    fieldsets = ((None, {'fields': ('email', 'username', 'password',)}),
                 ('Important dates', {'fields': ('last_login',)},))

    add_fieldsets = ((None, {'fields': ('email', 'username', 'password1', 'password2',)}),)

    ordering = ('username',)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    list_display = ['email', 'first_name', 'last_name', 'short_bio']

    search_fields = ['first_name', 'last_name']
    ordering = ('user',)

