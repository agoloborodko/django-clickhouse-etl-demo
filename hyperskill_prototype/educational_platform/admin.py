from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import PrototypeTask, PrototypeUser


class PrototypeUserInline(admin.StackedInline):
    model = PrototypeUser
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = (PrototypeUserInline,)


admin.site.register(PrototypeTask)
admin.site.register(User, UserAdmin)
