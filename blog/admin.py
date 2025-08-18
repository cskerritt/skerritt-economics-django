from django.contrib import admin
from .models import Category, Post, CaseStudy

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ["name"]

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "category", "status", "featured", "published_date"]
    list_filter = ["status", "featured", "category", "created_date", "published_date"]
    search_fields = ["title", "content", "excerpt"]
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "published_date"
    ordering = ["-published_date"]
    
    fieldsets = (
        ("Content", {
            "fields": ("title", "slug", "author", "content", "excerpt")
        }),
        ("Categorization", {
            "fields": ("category", "tags")
        }),
        ("Publishing", {
            "fields": ("status", "featured", "published_date")
        }),
        ("SEO", {
            "fields": ("meta_description",),
            "classes": ("collapse",)
        })
    )

@admin.register(CaseStudy)
class CaseStudyAdmin(admin.ModelAdmin):
    list_display = ["title", "practice_area", "amount", "featured", "published"]
    list_filter = ["practice_area", "featured", "published"]
    search_fields = ["title", "background", "analysis"]
    prepopulated_fields = {"slug": ("title",)}
    
    fieldsets = (
        ("Basic Info", {
            "fields": ("title", "slug", "practice_area", "amount")
        }),
        ("Case Details", {
            "fields": ("background", "analysis", "challenges", "outcome")
        }),
        ("Display Options", {
            "fields": ("featured", "published")
        })
    )
