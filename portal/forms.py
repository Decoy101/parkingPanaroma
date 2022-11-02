
from django import forms

from .models import Customer, Parking

class DateInput(forms.DateInput):
    input_type = 'date'

class EntryForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('first_name','last_name','room_no','phone_no','check_in','check_out','car_manufacturer','car_model','car_plates','car_color','car_parking','vehicle_type','parking_booking')
        widgets = {
            'check_in': DateInput(),
            'check_out': DateInput()
        }