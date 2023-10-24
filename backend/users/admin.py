from django.contrib import admin
from .models import User


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_active",
    )
    list_filter = ("is_active", "is_staff", "is_superuser")
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        ("Персональная информация", {"fields": ("first_name", "last_name")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
    )
    search_fields = ("username", "email", "first_name", "last_name")
    ordering = ("username",)
