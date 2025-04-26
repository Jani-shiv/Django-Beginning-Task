from django.urls import path
from . import views

urlpatterns = [
    path('', views.array_display, name='array_display'),
]
