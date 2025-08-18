from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """Admin interface for CustomUser model."""
    
    list_display = [
        "username", "email", "first_name", "last_name",
        "is_staff", "email_verified", "date_joined"
    ]
    
    list_filter = [
        "is_staff", "is_superuser", "is_active",
        "email_verified", "newsletter_subscribed",
        "date_joined", "last_login"
    ]
    
    search_fields = ["username", "first_name", "last_name", "email", "company"]
    
    fieldsets = UserAdmin.fieldsets + (
        (_("Additional Info"), {
            "fields": (
                "phone_number", "company", "title", "bio", "avatar"
            )
        }),
        (_("Preferences"), {
            "fields": (
                "email_verified", "newsletter_subscribed", "notification_preferences"
            )
        }),
        (_("Timestamps"), {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",)
        }),
    )
    
    readonly_fields = ["created_at", "updated_at"]
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        (_("Additional Info"), {
            "fields": (
                "email", "first_name", "last_name",
                "phone_number", "company", "title"
            )
        }),
    )