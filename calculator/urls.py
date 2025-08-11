from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'calculator'

urlpatterns = [
    # Authentication
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register_view, name='register'),
    
    # Main views
    path('', views.dashboard_view, name='dashboard'),
    path('new/', views.calculator_view, name='calculator_new'),
    path('<int:scenario_id>/', views.calculator_view, name='calculator'),
    path('<int:scenario_id>/delete/', views.delete_scenario, name='delete_scenario'),
    
    # API endpoints
    path('api/<int:scenario_id>/calculate/', views.calculate_api, name='calculate_api'),
    path('api/<int:scenario_id>/manual-offset/', views.save_manual_offset, name='save_manual_offset'),
    path('api/<int:scenario_id>/import-actuals/', views.import_actuals, name='import_actuals'),
    
    # Export/Import
    path('<int:scenario_id>/export/<str:table_type>/', views.export_csv, name='export_csv'),
    path('<int:scenario_id>/export-scenario/', views.export_scenario, name='export_scenario'),
    path('import-scenario/', views.import_scenario, name='import_scenario'),
]