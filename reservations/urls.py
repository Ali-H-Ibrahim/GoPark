from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.reservations_main, name='reservations-home'),
    path('view', views.showReservations, name='show-reservations'),
    path('customer-reservations/<str:pk>', views.customerReservationsPage, name='customer-reservations'),
    path('add', views.addReservation, name='add-reservation'),
    path('update/<str:pk>', views.updateReservation, name='update-reservation'),
    path('delete/<str:pk>', views.deleteReservation, name='delete-reservation'),

    path('api/', include('reservations.api.urls'))
]