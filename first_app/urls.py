from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.about, name="about"),
    path('contact-us/', views.contactus, name="contactus"),
    path('services/', views.services, name="services"),
]