"""
Production settings for Skerritt Economics website
"""
import os
from pathlib import Path
from .settings import *

# Override development settings for production
DEBUG = os.environ.get("DJANGO_DEBUG", "False") == "True"

# Security settings - SECRET_KEY is required in production
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")
if not SECRET_KEY:
    raise ValueError(
        "DJANGO_SECRET_KEY environment variable must be set in production. "
        "Generate a secure key using: python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'"
    )

# Parse ALLOWED_HOSTS, handling empty strings and whitespace
allowed_hosts_env = os.environ.get("DJANGO_ALLOWED_HOSTS", "skerritteconomics.com,www.skerritteconomics.com,localhost")
ALLOWED_HOSTS = [host.strip() for host in allowed_hosts_env.split(",") if host.strip()]

# Database - use SQLite for simplicity on Lightsail
# Determine the best database path based on environment
if os.path.exists("/app/db"):
    db_path = "/app/db/db.sqlite3"
elif os.path.exists("/home/bitnami/skerritt-economics-django"):
    db_path = "/home/bitnami/skerritt-economics-django/db.sqlite3"
else:
    db_path = os.path.join(BASE_DIR, "db.sqlite3")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": db_path,
    }
}

# Static files configuration
STATIC_URL = "/static/"
# Determine the best static files path based on environment
if os.path.exists("/app"):
    STATIC_ROOT = os.environ.get("STATIC_ROOT", "/app/staticfiles")
    MEDIA_ROOT = os.environ.get("MEDIA_ROOT", "/app/media")
elif os.path.exists("/home/bitnami/skerritt-economics-django"):
    STATIC_ROOT = os.environ.get("STATIC_ROOT", "/home/bitnami/skerritt-economics-django/staticfiles")
    MEDIA_ROOT = os.environ.get("MEDIA_ROOT", "/home/bitnami/skerritt-economics-django/media")
else:
    STATIC_ROOT = os.environ.get("STATIC_ROOT", os.path.join(BASE_DIR, "staticfiles"))
    MEDIA_ROOT = os.environ.get("MEDIA_ROOT", os.path.join(BASE_DIR, "media"))

MEDIA_URL = "/media/"

# Security
# Disable SSL redirect by default for initial setup, enable in production
SECURE_SSL_REDIRECT = os.environ.get("SECURE_SSL_REDIRECT", "False") == "True"
SESSION_COOKIE_SECURE = os.environ.get("SESSION_COOKIE_SECURE", "False") == "True"
CSRF_COOKIE_SECURE = os.environ.get("CSRF_COOKIE_SECURE", "False") == "True"
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
X_FRAME_OPTIONS = "DENY"

# Email configuration
EMAIL_BACKEND = os.environ.get("EMAIL_BACKEND", "django.core.mail.backends.smtp.EmailBackend")
EMAIL_HOST = os.environ.get("EMAIL_HOST", "smtp.gmail.com")
EMAIL_PORT = int(os.environ.get("EMAIL_PORT", 587))
EMAIL_USE_TLS = os.environ.get("EMAIL_USE_TLS", "True") == "True"
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", "")
DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL", "noreply@skerritteconomics.com")

# Logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "verbose"
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
    },
}

# Cache configuration
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "unique-snowflake",
    }
}

# Trusted origins for CSRF
CSRF_TRUSTED_ORIGINS = [
    "https://skerritteconomics.com",
    "https://www.skerritteconomics.com",
]