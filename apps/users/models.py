"""
Custom user model as per CLAUDE.md guidelines.
This should be imported directly in other parts of the application.
"""

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.utils.models import BaseModel


class CustomUser(AbstractUser, BaseModel):
    """
    Custom user model extending Django's AbstractUser.
    Includes timestamps from BaseModel.
    """
    
    # Additional fields
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        verbose_name=_("Phone number")
    )
    
    company = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("Company")
    )
    
    title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("Job title")
    )
    
    bio = models.TextField(
        blank=True,
        verbose_name=_("Biography")
    )
    
    avatar = models.ImageField(
        upload_to="avatars/",
        blank=True,
        null=True,
        verbose_name=_("Avatar")
    )
    
    email_verified = models.BooleanField(
        default=False,
        verbose_name=_("Email verified")
    )
    
    # Preferences
    newsletter_subscribed = models.BooleanField(
        default=False,
        verbose_name=_("Newsletter subscription")
    )
    
    notification_preferences = models.JSONField(
        default=dict,
        blank=True,
        verbose_name=_("Notification preferences")
    )

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ["-date_joined"]

    def __str__(self):
        return self.get_full_name() or self.username
    
    @property
    def full_name(self):
        """Return the user's full name."""
        return self.get_full_name()