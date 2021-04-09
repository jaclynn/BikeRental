from django.db import models
import datetime

BASE_PRICE = 25.00
TANDEM_SURCHARGE = 15.00
ELECTRIC_SURCHARGE = 25.00


# Create your models here.
class Bike(models.Model):
    ELECTRIC = "EL"
    STANDARD = "ST"
    TANDEM = "TA"
    BIKE_TYPE_CHOICES = [
        (ELECTRIC, 'Electric'),
        (STANDARD, 'Standard'),
        (TANDEM, 'Tandem'),
    ]
    bike_type = models.CharField(max_length=2, choices=BIKE_TYPE_CHOICES, default=STANDARD)
    lot_num = models.IntegerField(default=-1)
    bike_color = models.CharField(max_length=10, default="")

    def __str__(self):
        return str(self.lot_num) + ' ' + self.bike_type + ' ' + self.bike_color


class Renter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    vip_num = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.phone


class Rental(models.Model):
    AM = 'AM'
    PM = 'PM'
    AMPM_CHOICES = [(AM, 'AM'), (PM, 'PM')]
    renter = models.ForeignKey(Renter, on_delete=models.CASCADE)
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    ampm = models.CharField(max_length=2, choices=AMPM_CHOICES, default=AM)
    date = models.DateField(default=datetime.date.today)
    price = models.FloatField(default=0.0)

    def calc_price(self):
        p = BASE_PRICE  # base price
        if self.bike.bike_type == self.bike.TANDEM:
            p += TANDEM_SURCHARGE
        if self.bike.bike_type == self.bike.ELECTRIC:
            p += ELECTRIC_SURCHARGE
        if self.renter.vip_num > 0:
            p *= 0.8
        self.price = p
