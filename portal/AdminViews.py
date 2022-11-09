import datetime
from sqlite3 import Timestamp
from django.contrib import messages
from django.shortcuts import HttpResponse, get_object_or_404, redirect, render
from django.views.generic import ListView
from django.db.models import Subquery, F,Sum, Q
from django.db.models import Count
from portal.forms import EntryForm
from django.contrib.auth import logout

from .models import Reservation, CustomUser, Parking, Staffs,Connection
import time
import datetime
import pytz


utc=pytz.UTC


def Admin_HomePage(request):
    if not request.user.is_authenticated:
        logout(request)
        return redirect('login')
    else:
        return render(request,'admin_templates/home.html')
    
def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')
    else:
        return render(request,'admin_templates/home.html')

def add_staff(request):
    return render(request, 'admin_templates/add_staff.html')

def add_staff_save(request):
    if request.method != 'POST':
        messages.error(request,'Invalid Method')
        return redirect('add_staff')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')

        try:
            user = CustomUser.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name,user_type=2)
            user.address = address
            user.save()
            messages.success(request,"Staff added successfully")
            return redirect('add_staff')
        except:
            messages.error(request,"Failed to add staff")
            return redirect('add_staff')

def manage_staff(request):
    staffs = Staffs.objects.all()

    context = {
        "staffs" : staffs,

    }
    return render(request,'admin_templates/manage_staff.html',context)

def edit_staff(request,staff_id):
    staff = Staffs.objects.get(admin=staff_id)

    context = {
        "staff":staff,
        "id": staff_id
    }
    return render(request,'admin_templates/edit_staff.html',context)

def edit_staff_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        staff_id = request.POST.get('staff_id')
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')

        try:
            # INSERTING into Customuser Model
            user = CustomUser.objects.get(id=staff_id)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.username = username
            user.save()
            
            # INSERTING into Staff Model
            staff_model = Staffs.objects.get(admin=staff_id)
            staff_model.address = address
            staff_model.save()

            messages.success(request, "Staff Updated Successfully.")
            return redirect('manage_staff')

        except:
            messages.error(request, "Failed to Update Staff.")
            return redirect('/edit_staff/'+staff_id)



def delete_staff(request,staff_id):
    staff = Staffs.objects.get(admin=staff_id)
    try:
        staff.delete()
        messages.success(request,"Staff Deleted Successfully")
        return redirect('manage_staff')
    except:
        messages.error(request,'Failed to delete staff')
        return redirect('manage_staff')

def new_entry(request): 
    form = EntryForm
    return render(request,'admin_templates/new_entry.html',{'form':form})

def new_entry_save(request):
    if request.method != 'POST':
        messages.error(request,'Invalid Request')
        return redirect('new_entry')
    else:
        form = EntryForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            room_no =form.cleaned_data['room_no']
            phone_no =form.cleaned_data['phone_no']
            check_in =form.cleaned_data['check_in']
            check_out =form.cleaned_data['check_out']
            car_manufacturer =form.cleaned_data['car_manufacturer']
            car_model = form.cleaned_data['car_model']
            car_plates = form.cleaned_data['car_plates']
            car_color = form.cleaned_data['car_color']
            car_parking = form.cleaned_data['car_parking']
            vehicle_type = form.cleaned_data['vehicle_type']
            parking_booking = form.cleaned_data['parking_booking']
        
        try:
            customer = Reservation.objects.create(first_name = first_name,last_name = last_name,phone_no = phone_no, room_no = room_no,check_in = check_in,check_out = check_out,car_manufacturer = car_manufacturer,car_model=car_model,car_color = car_color,car_plates=car_plates,car_parking = car_parking,vehicle_type = vehicle_type,parking_booking = parking_booking)
            Reservation.save(customer)
            reservation_id = Reservation.objects.latest('id').id
            parking_id = Reservation.objects.get(id=reservation_id).car_parking.id
            connection = Connection.objects.create(parking_id= Parking.objects.get(id=parking_id),reservation_id=Reservation.objects.get(id=reservation_id))
            Connection.save(connection)
            messages.success(request,"Entry Added")
            return redirect('new_entry')
        except:
            messages.error(request,'Failed to add new entry')
            return redirect('new_entry')
        
def edit_entry(request,entry_id):
    entry = Reservation.objects.get(id = entry_id)
    parking_options = Reservation.objects.all()
    context = {
        'entry':entry,
        'parking_options': parking_options
    }
    return render(request,'admin_templates/edit_entry.html',context)


def edit_entry_save(request):
    entry_id = request.POST.get('entry_id')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    phone_no = request.POST.get('phone_no')
    room_no = request.POST.get('room_no')
    check_in = request.POST.get('check_in')
    check_out = request.POST.get('check_out')
    car_manufacturer = request.POST.get('car_manufacturer')
    car_model = request.POST.get('car_model')
    car_color = request.POST.get('car_color')
    car_plates = request.POST.get('car_plates')
    car_parking = request.POST.get('car_parking')
    vehicle_type = request.POST.get('vehicle_type')
    parking_booking = request.POST.get('parking_booking')
    
    entry = Reservation.objects.get(id=entry_id)
    entry.first_name = first_name
    entry.last_name = last_name
    entry.phone_no = phone_no
    entry.room_no = room_no
    entry.check_in = check_in
    entry.check_out = check_out
    entry.car_manufacturer = car_manufacturer
    entry.car_model = car_model
    entry.car_color = car_color
    entry.car_plates = car_plates
    entry.car_parking = car_parking
    entry.vehicle_type = vehicle_type
    entry.parking_booking = parking_booking
    entry.save()

    messages.success(request,'Entry Updated')
    return redirect('dashboard')
        

    
        

def delete_entry(request,entry_id):
    entry = Reservation.objects.get(id=entry_id)
    try:
        if entry.parking_booking == 'YES':
            delete_prebooking(entry.car_parking)

        entry.delete()

        messages.success(request,"Entry Deleted Successfully")
        return redirect('dashboard')
    except:
        messages.error(request,'Parking to delete staff')
        return redirect('dashboard')

def add_parking(request):
    return render(request,'admin_templates/add_parking_info.html')

def add_parking_save(request):
    if request.method != 'POST':
        messages.error(request,"Invalid Request")
        return redirect('add_parking')
    else:
        parking_name = request.POST.get('parking_name')
        total_spaces = request.POST.get('parking_available')
        max_car_spaces = request.POST.get('max_car_spaces')
        max_bike_spaces = request.POST.get('max_bike_spaces')

        try:
            parking = Parking.objects.create(name=parking_name,total=total_spaces,max_car = max_car_spaces,max_bike = max_bike_spaces)
            Parking.save(parking)
            messages.success(request,'Parking Space Added')
            return redirect('add_parking')
        except:
            messages.error(request,'Failed to add new entry')
            return redirect('add_parking')

def edit_parking(request,parking_id):
    parking = Parking.objects.get(id=parking_id)
    context = {
        'parking':parking,
        'id':parking_id
    }
    return render(request,'admin_templates/edit_parking.html',context)
    
       
    
def edit_parking_save(request):
    if request.method != 'POST':
        messages.error(request,'Invalid Request')
    else:
        parking_id = request.POST.get('parking_id')
        name = request.POST.get('name')
        total = request.POST.get('total_spaces')
        max_car = request.POST.get('max_car')
        max_bike = request.POST.get('max_bike')
        car_spots_reserved = request.POST.get('car_spots_reserved')
        bike_spots_reserved = request.POST.get('bike_spots_reserved')
        parking = Parking.objects.get(id=parking_id)
        parking.name = name
        parking.total = total
        parking.max_car = max_car
        parking.max_bike = max_bike
        parking.car_spots_reserved = car_spots_reserved
        parking.bike_spots_reserved = bike_spots_reserved
        parking.save()
        parking.available = int(parking.total) - (int(parking.car_spots_reserved)+ int(parking.bike_spots_reserved))
        parking.save()

        messages.success(request,'Parking Updated Successfully')
        return redirect('parking')
        


def delete_parking(request,parking_id):
    parking = Parking.objects.get(id=parking_id)
    try:
        parking.delete()
        messages.success(request,"Parking Deleted Successfully")
        return redirect('parking')
    except:
        messages.error(request,'Parking to delete staff')
        return redirect('parking') 

def ReservationListView(request):
    reservations = Reservation.objects.all()
    parking_options = Parking.objects.all()

    context = {
        "reservations": reservations,
        "parking_options": parking_options
    }

    return render(request,'admin_templates/dashboard.html',context)


def ParkingListView(request):
    date = datetime.datetime.today().strftime("%Y-%m-%d")
    parking_options = Parking.objects.annotate(prebooking=Count('parking',filter=Q(parking__check_in=date,parking__is_checked_in=False,parking__parking_booking='Yes')))
    parking_options = parking_options.annotate(car_spots_reserved=Count('parking',filter=Q(parking__is_checked_in=True,parking__vehicle_type='CAR',parking__is_checked_out=False,parking__parking_booking='Yes')))
    parking_options = parking_options.annotate(bike_spots_reserved=Count('parking',filter=Q(parking__is_checked_in=True,parking__vehicle_type='BIKE',parking__is_checked_out=False,parking__parking_booking='Yes')))
    parking_options = parking_options.annotate(available=F('total')-F('car_spots_reserved')-F('bike_spots_reserved')-F('prebooking'))
   
    context = {
        'parking_options': parking_options,
    }
    return render(request,'admin_templates/parking.html',context)


def customer_view(request,reservation_id):
    customer = get_object_or_404(Reservation,id = reservation_id)
    return render(request,'admin_templates/customer_details.html',locals())

# the sequeces of the Parking Objects are yet to fixed

    

        
            
def update_status(request):
    if request.method == 'POST':
        customer_id = request.POST['customer_id']
        status = request.POST['status']
        if status=='in':
            Reservation.objects.filter(pk=customer_id).update(is_checked_in = 1)
        else:
            Reservation.objects.filter(pk=customer_id).update(is_checked_out = 1)

        return HttpResponse('Success')
    return HttpResponse("Failure")

def delete_prebooking(name):
    count = Parking.objects.latest('id').id
    for i in range(1,count+1):
        try:
            if Parking.objects.get(id=i).name == name:
                Parking.objects.filter(pk=i).update(preBooking = Parking.objects.get(id=i).preBooking - 1 )
        except:
            pass

                            
# def prebooking_update():
#     count = Customer.objects.latest('id').id
#     for i in range(1,count+1):
#         try:
#             customer = Customer.objects.get(id=i) 
#             if customer.prebooking_marked == False:
#                 if customer.parking_booking == "Yes":
#                     if datetime.datetime.today().timestamp() >= customer.check_in.timestamp():
#                         customer.prebooking_marked = True
#                         customer.car_parking.preBooking +=1
#                         customer.car_parking.available -=1
#                         customer.prebooking_marked  = 1
#                         customer.car_parking.save() 
#         except:
#             pass
    
# def prebooking_update(date):
#     reservations = Customer.objects.all().filter(check_in__exact=date).values('car_parking').annotate(prebooking_count=Count('car_parking'))
#     

    

# def prebooking_update(request,date):
#     reservations = Customer.objects.all().filter(check_in__exact=date).values('car_parking').annotate(prebooking_count=Count('car_parking'))
#     parking_spots = Parking.objects.all()
#     for parking in parking_spots:
#         parking.preBooking = 0
#         parking.save()

#     for reservation in reservations:
#         Parking.objects.filter(id=int(reservation['car_parking'])).update(preBooking=int(reservation['prebooking_count']))
#     return render(request,'admin_templates/parking.html')
    

    

        
    
