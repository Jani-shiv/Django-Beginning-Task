from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
]
