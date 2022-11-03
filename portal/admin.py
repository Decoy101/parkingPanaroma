from django.contrib import admin

# Register your models here.
from .models import Reservation, CustomUser, Admin, Staffs, Parking

admin.site.register(Reservation);
admin.site.register(CustomUser);
admin.site.register(Admin);
admin.site.register(Staffs);
admin.site.register(Parking);



