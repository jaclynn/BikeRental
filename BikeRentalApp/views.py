import datetime
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Bike, Renter, Rental
from .forms import BikeCreateForm, RenterCreateForm, RentalCreateForm


# Create your views here.
def home(request):
    return render(request, 'BikeRentalApp/home.html')


class BikeList(ListView):
    model = Bike


class RenterList(ListView):
    model = Renter


class RentalList(ListView):
    model = Rental


class BikeCreate(CreateView):
    model = Bike
    template_name = 'BikeRentalApp/bike_create_form.html'
    form_class = BikeCreateForm
    success_url = '/bike/list'

    def form_valid(self, form):
        return super().form_valid(form)


class RenterCreate(CreateView):
    model = Renter
    template_name = 'BikeRentalApp/renter_create_form.html'
    form_class = RenterCreateForm
    success_url = '/renter/list'

    def form_valid(self, form):
        return super().form_valid(form)


class RentalCreate(CreateView):
    model = Rental
    template_name = 'BikeRentalApp/rental_create_form.html'
    form_class = RentalCreateForm
    success_url = '/rental/list'

    def form_valid(self, form):
        form.instance.calc_price()
        return super().form_valid(form)
