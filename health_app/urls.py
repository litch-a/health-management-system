from django.urls import path
from . import views 

app_name = 'health_app'  #Set the app_name for namespacing

urlpatterns = [
path('dashboard-content/', views.dashboard_content, name='dashboard_content'),
path('register-client-content/', views.register_client_content, name='register_client_content'),
path('create-health-program-content/', views.create_health_program_content, name='create_health_program_content'),
path('clients-list-content/', views.clients_list_content, name='clients_list_content'),
path('health-programs-list-content/', views.health_programs_list_content, name='health_programs_list_content'),
path('enroll-client-content/', views.enroll_client_content, name='enroll_client_content'),

]