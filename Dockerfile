# Multi-stage build for Tailwind CSS
FROM node:20-alpine AS tailwind-builder

WORKDIR /app

# Copy package files
COPY package.json tailwind.config.js ./
COPY static/css/tailwind-input.css ./static/css/

# Install dependencies and build Tailwind
RUN npm install && \
    npx tailwindcss -i ./static/css/tailwind-input.css -o ./static/css/tailwind-output.css --minify

# Main Python image
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

# Install gunicorn for production and development tools
RUN pip install --no-cache-dir gunicorn ruff

# Copy project
COPY . .

# Copy built Tailwind CSS from builder stage
COPY --from=tailwind-builder /app/static/css/tailwind-output.css /app/static/css/tailwind-output.css

# Create user for security
RUN useradd -m -u 1000 django && chown -R django:django /app

# Create static, media and db directories
RUN mkdir -p /app/staticfiles /app/media /app/db && \
    chown -R django:django /app/staticfiles /app/media /app/db

USER django

# Note: collectstatic is run at runtime via entrypoint script
# to ensure environment variables are available

# Create entrypoint script
RUN echo '#!/bin/bash\n\
set -e\n\
echo "Collecting static files..."\n\
python manage.py collectstatic --noinput\n\
echo "Starting Gunicorn..."\n\
exec gunicorn --bind 0.0.0.0:8000 --workers 2 --threads 4 --worker-class gthread --worker-tmp-dir /dev/shm --log-file - --access-logfile - --error-logfile - skerritt_site.wsgi:application' > /app/entrypoint.sh && \
chmod +x /app/entrypoint.sh

# Run entrypoint script
CMD ["/app/entrypoint.sh"]