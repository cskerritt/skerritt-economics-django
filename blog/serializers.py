"""
Serializers for blog app API endpoints.
"""

from rest_framework import serializers
from .models import Post, CaseStudy


class PostSerializer(serializers.ModelSerializer):
    """Serializer for Post model."""
    author_name = serializers.CharField(source="author.get_full_name", read_only=True)
    
    class Meta:
        model = Post
        fields = [
            "id", "title", "slug", "author", "author_name",
            "content", "excerpt", "status", "published_date", "created_date",
            "updated_date", "meta_description"
        ]
        read_only_fields = ["slug", "created_date", "updated_date"]


class CaseStudySerializer(serializers.ModelSerializer):
    """Serializer for CaseStudy model."""
    
    class Meta:
        model = CaseStudy
        fields = [
            "id", "name", "case_type", "description",
            "amount", "outcome", "created_date", "featured"
        ]
        read_only_fields = ["created_date"]