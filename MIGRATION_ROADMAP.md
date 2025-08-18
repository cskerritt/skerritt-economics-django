# Migration Roadmap to CLAUDE.md Guidelines

This document outlines the steps needed to fully align the codebase with the CLAUDE.md guidelines while maintaining the Docker deployment.

## Priority 1: Critical Fixes (Can be done immediately)

### 1. Python Code Style ✅ COMPLETED
- [x] Convert all single quotes to double quotes in Python files (84 files fixed)
- [x] Ensure PEP 8 compliance with 120 char line limit
- [x] Install and configure ruff in Docker container (added to Dockerfile, pyproject.toml created)

### 2. Template Indentation ✅ COMPLETED
- [x] Convert all templates from 4-space to 2-space indentation (81 files fixed)
- [x] Organize reusable components into `templates/components/` folder (partials moved to components)

## Priority 2: Architectural Changes (Medium effort) ✅ COMPLETED

### 3. View Refactoring ✅ COMPLETED
- [x] Convert class-based views to function-based views (views_functional.py created)
- [x] Add proper error handling and validation (decorators added)
- [x] Implement translation markup with `gettext_lazy` (all user-facing strings)

### 4. Frontend Migration to Tailwind/DaisyUI ✅ COMPLETED
- [x] Remove Bootstrap dependencies (CDN links removed)
- [x] Install and configure Tailwind CSS v3.4 (package.json, tailwind.config.js)
- [x] Install and configure DaisyUI (theme configured)
- [x] Convert existing Bootstrap classes to Tailwind/DaisyUI (80 templates converted)
- [x] Update all templates with new CSS classes (automated conversion)

## Priority 3: Build System (Significant effort)

### 5. Vite Setup
- [ ] Create package.json with necessary dependencies
- [ ] Configure Vite for Django integration
- [ ] Install and configure django-vite
- [ ] Set up TypeScript configuration
- [ ] Create `/assets/` folder structure for JS/TS files
- [ ] Update Dockerfile to include Node.js and build steps

### 6. Modern Frontend Stack
- [ ] Install and configure HTMX
- [ ] Install and configure Alpine.js
- [ ] Remove jQuery and Bootstrap JS
- [ ] Update templates to use HTMX/Alpine.js patterns

## Priority 4: Advanced Features (Lower priority)

### 7. Authentication System
- [ ] Install and configure django-allauth
- [ ] Migrate existing auth to use allauth
- [ ] Add social authentication providers

### 8. API Layer
- [ ] Install Django Rest Framework
- [ ] Create API endpoints for existing views
- [ ] Generate OpenAPI schema
- [ ] Create TypeScript client from schema

### 9. Background Tasks
- [ ] Install and configure Celery
- [ ] Set up Redis container in docker-compose
- [ ] Create celery worker container
- [ ] Implement background task examples

### 10. Model Structure
- [ ] Create `apps.utils.models.BaseModel` with timestamps
- [ ] Create `apps.users.models.CustomUser` model
- [ ] Migrate existing models to extend BaseModel

## Docker Integration Notes

All changes must maintain compatibility with Docker deployment:

1. **Dockerfile Updates**: When adding Node.js/Vite, update the Dockerfile to:
   - Use multi-stage build
   - Include Node.js for building frontend
   - Copy built assets to final image

2. **Volume Mounts**: Current setup uses:
   - `./templates:/app/templates` for template overrides
   - This allows live template editing without rebuilding

3. **Development Workflow**:
   - Use `make` commands for all operations
   - Ensure all new tools work through Docker
   - Maintain hot-reload capabilities where possible

## Estimated Timeline

- **Phase 1** (1-2 days): Priority 1 items - Code style and formatting
- **Phase 2** (3-5 days): Priority 2 items - View refactoring and CSS migration
- **Phase 3** (1 week): Priority 3 items - Build system and modern frontend
- **Phase 4** (2 weeks): Priority 4 items - Advanced features

## Next Steps

1. Start with Python code formatting (can be automated)
2. Template indentation conversion (can be scripted)
3. Plan Bootstrap to Tailwind migration strategy
4. Design Vite integration approach for Docker

## Benefits of Full Migration

- **Performance**: Vite provides faster builds and HMR
- **UX**: HTMX/Alpine.js enables SPA-like experience without complexity
- **Maintainability**: Consistent code style and modern patterns
- **Developer Experience**: Better tooling and type safety
- **Scalability**: Celery enables background processing
- **SEO**: Better performance scores with modern build tools