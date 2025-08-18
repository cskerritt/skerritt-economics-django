"""
Base model with timestamps as per CLAUDE.md guidelines.
All Django models should extend this BaseModel.
"""

from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    """
    Abstract base model that adds created_at and updated_at fields.
    All models in the project should inherit from this.
    """
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created at"),
        help_text=_("Date and time when the record was created")
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Updated at"),
        help_text=_("Date and time when the record was last updated")
    )

    class Meta:
        abstract = True
        ordering = ["-created_at"]