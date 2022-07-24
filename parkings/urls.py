from django.urls import path
from . import views


urlpatterns = [
    path('addCarParking', views.addCarParking, name='add-car-parking')
]