from django.urls import path
from . import views 

app_name = 'health_app'  #Set the app_name for namespacing

urlpatterns = [
    path('', views.index, name='index'),
]