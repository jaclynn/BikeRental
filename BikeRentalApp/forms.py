from django import forms
from .models import Bike, Renter, Rental


class RenterCreateForm(forms.ModelForm):
    class Meta:
        model = Renter
        fields = ('first_name', 'last_name', 'phone', 'vip_num')


class RentalCreateForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ('bike', 'renter', 'date', 'ampm')

class BikeCreateForm(forms.ModelForm):
    class Meta:
        model = Bike
        fields = ('lot_num', 'bike_type', 'bike_color')