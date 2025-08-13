from django.urls import path
from . import location_views

app_name = 'locations'

urlpatterns = [
    # Main locations index
    path('', location_views.all_locations, name='index'),
    
    # Major city pages
    path('boston/', location_views.location_detail, {'location_slug': 'boston'}, name='boston'),
    path('providence/', location_views.location_detail, {'location_slug': 'providence'}, name='providence'),
    path('hartford/', location_views.location_detail, {'location_slug': 'hartford'}, name='hartford'),
    path('portland/', location_views.location_detail, {'location_slug': 'portland'}, name='portland'),
    path('burlington/', location_views.location_detail, {'location_slug': 'burlington'}, name='burlington'),
    path('manchester/', location_views.location_detail, {'location_slug': 'manchester'}, name='manchester'),
    
    # Generic location handler
    path('<slug:location_slug>/', location_views.location_detail, name='detail'),
]