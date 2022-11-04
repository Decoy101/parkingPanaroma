from django.contrib import admin

# Register your models here.
from .models import Customer, CustomUser, Admin, Staffs, Parking

admin.site.register(Customer);
admin.site.register(CustomUser);
admin.site.register(Admin);
admin.site.register(Staffs);
admin.site.register(Parking);



