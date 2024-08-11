from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
User = get_user_model()


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_superuser','is_staff')


admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
