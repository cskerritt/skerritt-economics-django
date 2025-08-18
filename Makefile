.PHONY: help start stop restart shell dbshell manage test migrate makemigrations collectstatic logs ssh clean

# Default target
help:
	@echo "Available commands:"
	@echo "  make start          - Start all services with Docker Compose"
	@echo "  make start-bg       - Start all services in background"
	@echo "  make stop           - Stop all services"
	@echo "  make restart        - Restart all services"
	@echo "  make shell          - Open Django shell"
	@echo "  make dbshell        - Open database shell"
	@echo "  make manage         - Run Django management command (use ARGS='command')"
	@echo "  make test           - Run all tests"
	@echo "  make migrate        - Run database migrations"
	@echo "  make makemigrations - Create new migrations"
	@echo "  make collectstatic  - Collect static files"
	@echo "  make logs           - View container logs"
	@echo "  make ssh            - SSH into Django container"
	@echo "  make clean          - Clean up containers and volumes"
	@echo "  make ruff-lint      - Run Python linter"
	@echo "  make ruff-format    - Format Python code"
	@echo "  make npm-build      - Build frontend assets (when implemented)"
	@echo "  make npm-dev        - Start frontend dev server (when implemented)"

# Docker commands
start:
	docker compose up

start-bg:
	docker compose up -d

stop:
	docker compose down

restart:
	docker compose restart

# Django commands
shell:
	docker exec -it skerritt_django python manage.py shell

dbshell:
	docker exec -it skerritt_django python manage.py dbshell

manage:
	docker exec skerritt_django python manage.py $(ARGS)

test:
ifdef ARGS
	docker exec skerritt_django python manage.py test $(ARGS)
else
	docker exec skerritt_django python manage.py test
endif

migrate:
	docker exec skerritt_django python manage.py migrate

makemigrations:
	docker exec skerritt_django python manage.py makemigrations

collectstatic:
	docker exec skerritt_django python manage.py collectstatic --noinput

# Utility commands
logs:
	docker compose logs -f

ssh:
	docker exec -it skerritt_django /bin/bash

clean:
	docker compose down -v
	docker system prune -f

# Python linting and formatting (requires ruff in container)
ruff-lint:
	docker exec skerritt_django ruff check . || echo "Ruff not installed in container"

ruff-format:
	docker exec skerritt_django ruff format . || echo "Ruff not installed in container"

# Frontend commands (placeholders for when Vite is set up)
npm-build:
	@echo "Frontend build not yet configured. Vite needs to be set up."

npm-dev:
	@echo "Frontend dev server not yet configured. Vite needs to be set up."

npm-type-check:
	@echo "TypeScript not yet configured."

# Translation commands
translations:
	docker exec skerritt_django python manage.py makemessages -a
	docker exec skerritt_django python manage.py compilemessages