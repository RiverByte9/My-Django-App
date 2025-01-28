from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Maps the home function to the root URL
]
