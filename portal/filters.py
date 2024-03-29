import django_filters
from django import forms

from .models import Parking, Reservation

class DateInput(forms.DateInput):
    input_type = 'date'

class ReservationsFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    check_in = django_filters.DateFilter(widget=DateInput(attrs={'type': 'date'}))
    check_out = django_filters.DateFilter(widget=DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Reservation
        fields = '__all__'
        exclude = ['room_no','phone_no']
