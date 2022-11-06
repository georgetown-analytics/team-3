from django.urls import path
from . import views

#URLConfiguration
urlpatterns = [
    path('home/', views.home)
]