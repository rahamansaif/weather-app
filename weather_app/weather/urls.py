from django.urls import path

from weather import views


urlpatterns = [
    path('', views.index),
    path('<int:id>', views.weather_details),
]