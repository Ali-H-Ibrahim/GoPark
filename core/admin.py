from django.contrib import admin
from .models import Permission, Brand, Park, CarParking, Car, History, Reservation, User

admin.site.register(Permission)
admin.site.register(Brand)
admin.site.register(Park)
admin.site.register(CarParking)
admin.site.register(Car)
admin.site.register(History)
admin.site.register(Reservation)
admin.site.register(User)