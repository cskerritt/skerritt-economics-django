"""
API URL configuration.
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from blog.api_views import PostViewSet, CaseStudyViewSet

# Create router and register viewsets
router = DefaultRouter()
router.register(r"blog-posts", PostViewSet, basename="post")
router.register(r"case-studies", CaseStudyViewSet, basename="casestudy")

urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include("rest_framework.urls", namespace="rest_framework")),
]