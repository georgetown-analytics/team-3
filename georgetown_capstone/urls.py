from django.urls import path
from . import views

#URLConfiguration
urlpatterns = [
    path('', views.home, name="home"),
    path('results/', views.results, name="results"),
    path('database/', views.view_results, name='database'),
    
]