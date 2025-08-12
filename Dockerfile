# Use Python 3.11 slim image for smaller size
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive \
    DJANGO_SETTINGS_MODULE=skerritt_site.settings_production

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    postgresql-client \
    netcat-openbsd \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install gunicorn for production
RUN pip install --no-cache-dir gunicorn

# Copy project
COPY . .

# Create user for security
RUN useradd -m -u 1000 django && chown -R django:django /app

# Create static, media and db directories
RUN mkdir -p /app/staticfiles /app/media /app/db && \
    chown -R django:django /app/staticfiles /app/media /app/db

USER django

# Collect static files
RUN python manage.py collectstatic --noinput

# Run gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "2", "--threads", "4", "--worker-class", "gthread", "--worker-tmp-dir", "/dev/shm", "--log-file", "-", "--access-logfile", "-", "--error-logfile", "-", "skerritt_site.wsgi:application"]