from django.db import models
from django.contrib.auth.models import AbstractUser


class Permission(models.Model):
    PERMISSIONS_TYPES = (
        ('Garage Manager', 'Garage Manager'),
        ('Cashier', 'Cashier'),
        ('Customer', 'Customer'),
    )

    permission_type = models.CharField(max_length=100, choices=PERMISSIONS_TYPES)


class User(AbstractUser):
    permission   = models.ForeignKey(Permission, on_delete=models.SET_NULL, null=True, blank=True)

    first_name   = models.CharField(max_length=100)
    last_name    = models.CharField(max_length=100)
    email        = models.EmailField(unique=True, null=True)
    phone_number = models.CharField(max_length=100)
    avatar       = models.ImageField(null=True, blank=True)


    def __str__(self):
        return str(self.first_name)+' '+str(self.last_name)


class Brand(models.Model):
    name  = models.CharField(max_length=200, null=False)
    model = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.name)+' - '+str(self.model)


class Park(models.Model):
    name    = models.CharField(max_length=100, null=False, default='') 
    floor   = models.IntegerField(null=True, blank=True)
    size    = models.CharField(max_length=100, null=True, blank=True)
    is_free = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)+str(self.floor)


class Car(models.Model):
    owner       = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='users')
    brand       = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)

    plateNumber = models.CharField(max_length=100)
    color       = models.CharField(max_length=100)
    capacity    = models.IntegerField(null=True, blank=True)
    weight      = models.FloatField(null=True, blank=True)

    def __str__(self):
        return str(self.brand)+' - '+str(self.color)+' - '+str(self.plateNumber)


class CarParking(models.Model):
    car        = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)
    park       = models.OneToOneField(Park, on_delete=models.SET_NULL, null=True)
    entry_date = models.DateTimeField(auto_now_add=True)
    end_date   = models.DateTimeField()
    cost       = models.IntegerField()

    class Meta:
        ordering = ['-entry_date']

    def __str__(self):
        return str(self.park)


class History(models.Model):
    customer            = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    carParking          = models.ForeignKey(CarParking, on_delete=models.SET_NULL, null=True)
    total_parking_hours = models.DurationField()
    total_payments      = models.IntegerField()

    def __str__(self):
        return str(self.carParking)


class Reservation(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    park     = models.ForeignKey(Park, on_delete=models.SET_NULL, null=True)
    
    # make choices for reservation type then pass them to type field
    RESERVATION_TYPES = (
        ('One Time', 'One Time'),
        ('Daily', 'Daily'),
        ('Weekly', 'Weekly')
    )
    
    reservation_type = models.CharField(max_length=100, choices=RESERVATION_TYPES)
    reserved_period  = models.FloatField()  # by hours
    start_date       = models.DateTimeField()
    end_date         = models.DateField()
    cost             = models.IntegerField(null=True)

    class Meta:
        ordering = ['start_date']

    def __str__(self):
        return str(self.customer)+' - '+str(self.park)+' - '+str(self.reservation_type)
