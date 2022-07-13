from django.urls import path
from . import views


urlpatterns = [
    path('my-reservations', views.getUserReservations, name='user-reservations'),
    path('add', views.addReservation, name='add-reservation-api'),
    path('delete', views.deleteReservation, name='delete-reservation')
]