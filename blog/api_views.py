"""
API views for blog app.
"""

from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from .models import Post, CaseStudy
from .serializers import PostSerializer, CaseStudySerializer


class PostViewSet(viewsets.ModelViewSet):
    """API endpoint for blog posts."""
    queryset = Post.objects.filter(status="published")
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title", "content", "excerpt"]
    ordering_fields = ["created_date", "updated_date"]
    ordering = ["-created_date"]
    lookup_field = "slug"


class CaseStudyViewSet(viewsets.ModelViewSet):
    """API endpoint for case studies."""
    queryset = CaseStudy.objects.all()
    serializer_class = CaseStudySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ["case_type", "featured"]
    ordering_fields = ["created_date", "amount"]
    ordering = ["-featured", "-created_date"]