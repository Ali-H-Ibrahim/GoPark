from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    PERMISSIONS_TYPES = (
        ('Garage Manager', 'Garage Manager'),
        ('Cashier', 'Cashier'),
        ('Customer', 'Customer'),
    )
    permission = models.CharField(max_length=100, choices=PERMISSIONS_TYPES)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, null=True)
    phone_number = models.CharField(max_length=100)
    avatar = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name)


class Brand(models.Model):
    name = models.CharField(max_length=200, null=False)
    model = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.name) + ' - ' + str(self.model)


class Car(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='users')
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)

    plateNumber = models.CharField(max_length=100)
    color = models.CharField(max_length=100)

    def __str__(self):
        return str(self.brand) + ' - ' + str(self.color) + ' - ' + str(self.plateNumber)


class Floor(models.Model):
    floor_number = models.IntegerField(null=True, blank=True)
    size = models.IntegerField(null=True, blank=True)
    is_free = models.BooleanField(default=True)


class CarParking(models.Model):
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)
    floor = models.ForeignKey(Floor, on_delete=models.SET_NULL, null=True)

    entry_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    cost = models.IntegerField()

    class Meta:
        ordering = ['-entry_date']

    def __str__(self):
        return str(self.park)


class Reservation(models.Model):
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)
    car_parking = models.ForeignKey(CarParking, on_delete=models.SET_NULL, null=True)

    # make choices for reservation type then pass them to type field
    RESERVATION_TYPES = (
        ('One Time', 'One Time'),
        ('Daily', 'Daily'),
        ('Weekly', 'Weekly')
    )

    reservation_type = models.CharField(max_length=100, choices=RESERVATION_TYPES)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    cost = models.IntegerField(null=True)

    class Meta:
        ordering = ['start_date']

    def __str__(self):
        return str(self.car) + ' - ' + str(self.car_parking) + ' - ' + str(self.reservation_type)


class Payment(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.SET_NULL, null=True)
    PAYMENT_TYPES = (
        ('Cash', 'Cash'),
        ('MasterCard', 'MasterCard'),
        ('VisaCard', 'VisaCard'),
        ('PayPal', 'PayPal')
    )

    reservation_type = models.CharField(max_length=100, choices=PAYMENT_TYPES)



# class Park(models.Model):
#     name = models.CharField(max_length=100, null=False, default='')
#     floor = models.IntegerField(null=True, blank=True)
#     size = models.CharField(max_length=100, null=True, blank=True)
#     is_free = models.BooleanField(default=True)
#
#     def __str__(self):
#         return str(self.name) + str(self.floor)

# class History(models.Model):
#     customer = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
#     carParking = models.ForeignKey(CarParking, on_delete=models.SET_NULL, null=True)
#     total_parking_hours = models.DurationField()
#     total_payments = models.IntegerField()
#
#     def __str__(self):
#         return str(self.carParking)
