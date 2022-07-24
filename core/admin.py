from django.contrib import admin
from .models import Brand, CarParking, Car, Reservation, User, Floor, Payment

admin.site.register(Brand)
admin.site.register(CarParking)
admin.site.register(Car)
admin.site.register(Reservation)
admin.site.register(User)
admin.site.register(Floor)
admin.site.register(Payment)