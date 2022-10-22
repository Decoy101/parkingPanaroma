from email import message
from re import template
from tabnanny import check

from django.contrib import messages
from django.shortcuts import HttpResponse, get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView

from .models import Customer, CustomUser, Parking, Staffs


def Admin_HomePage(request):
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
    parking_options = Parking.objects.all()
    context = {
        "parking_options": parking_options
    }
    return render(request,'admin_templates/new_entry.html',context)

def new_entry_save(request):
    if request.method != 'POST':
        messages.error(request,'Invalid Request')
        return redirect('new_entry')
    else:
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

        
        try:
            customer = Customer.objects.create(first_name = first_name,last_name = last_name,phone_no = phone_no, room_no = room_no,check_in = check_in,check_out = check_out,car_manufacturer = car_manufacturer,car_model=car_model,car_color = car_color,car_plates=car_plates,car_parking = car_parking,vehicle_type = vehicle_type,parking_booking = parking_booking)
            Customer.save(customer)
            messages.success(request,"Entry Added")
            return redirect('new_entry')
        except:
            messages.error(request,'Failed to add new entry')
            return redirect('new_entry')
        
def edit_entry(request,entry_id):
    entry = Customer.objects.get(id = entry_id)
    parking_options = Customer.objects.all()
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
    
    entry = Customer.objects.get(id=entry_id)
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
    entry = Customer.objects.get(id=entry_id)
    try:
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
            return redirect('parking')
        except:
            messages.error(request,'Failed to add new entry')
            return redirect('parking')

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

class ReservationsListView(ListView):
    model = Customer
    template_name = 'admin_templates/dashboard.html'
    context_object_name = 'reservations'


def ReservationListView(request):
    reservations = Customer.objects.all()
    parking_options = Parking.objects.all()

    context = {
        "reservations": reservations,
        "parking_options": parking_options
    }

    return render(request,'admin_templates/dashboard.html',context)


class ParkingListView(ListView):
    model = Parking
    template_name = 'admin_templates/parking.html'




def customer_view(request,reservation_id):
    customer = get_object_or_404(Customer,id = reservation_id)
    return render(request,'admin_templates/customer_details.html',locals())

# the sequeces of the Parking Objects are yet to fixed
def update_parking(request):
    if request.method == 'POST':
        count = Parking.objects.latest('id').id
        
        parking = request.POST['parking'];
        vehicle_type = request.POST['vehicle_type']
        status = request.POST['status']
        for i in range(1,count+1):
            try:
                if Parking.objects.get(id=i).name == parking:
                    if status == 'in':
                        if vehicle_type == 'CAR':
                            Parking.objects.filter(pk=i).update(car_spots_reserved=Parking.objects.get(id=i).car_spots_reserved+1)
                        elif vehicle_type == 'BIKE':
                            Parking.objects.filter(pk=i).update(bike_spots_reserved=Parking.objects.get(id=i).bike_spots_reserved+1)
                    elif status == 'out':
                        if vehicle_type == 'CAR':
                            Parking.objects.filter(pk=i).update(car_spots_reserved=Parking.objects.get(id=i).car_spots_reserved-1)
                        elif vehicle_type == 'BIKE':
                            Parking.objects.filter(pk=i).update(bike_spots_reserved=Parking.objects.get(id=i).bike_spots_reserved-1)
                    Parking.objects.filter(pk=i).update(available=Parking.objects.get(id=i).total - (Parking.objects.get(id=i).car_spots_reserved + Parking.objects.get(id=i).bike_spots_reserved))
                    return HttpResponse('Success')
            except:
                pass
              
    return HttpResponse('Fail')  
        

            
def update_status(request):
    if request.method == 'POST':
        customer_id = request.POST['customer_id']
        status = request.POST['status']
        if status=='in':
            Customer.objects.filter(pk=customer_id).update(is_checked_in = 1)
        else:
            Customer.objects.filter(pk=customer_id).update(is_checked_out = 1)

        return HttpResponse('Success')
    return HttpResponse("Failure")