from django.urls import path
from . import views


urlpatterns = [
    path('add', views.addReservation, name='add-reservation-api'),
]