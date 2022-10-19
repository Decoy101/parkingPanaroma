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

        
def add_parking(request):
    return render(request,'admin_templates/add_parking_info.html')

def add_parking_save(request):
    if request.method != 'POST':
        messages.error(request,"Invalid Request")
        return redirect('add_parking')
    else:
        parking_name = request.POST.get('parking_name')
        total_spaces = request.POST.get('parking_available')

        try:
            parking = Parking.objects.create(name=parking_name,total=total_spaces)
            Parking.save(parking)
            messages.success(request,'Parking Space Added')
            return redirect('parking')
        except:
            messages.error(request,'Failed to add new entry')
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
        status = request.POST['status']
        for i in range(1,count+1):
            try:
                if Parking.objects.get(id=i).name == parking:
                    if status == 'in':
                        Parking.objects.filter(pk=i).update(reserved=Parking.objects.get(id=i).reserved+1);
                    elif status == 'out':
                        Parking.objects.filter(pk=i).update(reserved=Parking.objects.get(id=i).reserved-1);
                    Parking.objects.filter(pk=i).update(available=Parking.objects.get(id=i).total-Parking.objects.get(id=i).reserved);
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