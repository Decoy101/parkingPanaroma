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
    return render(request,'admin_templates/new_entry.html')

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
            return redirect('add_parking')
        except:
            messages.error(request,'Failed to add new entry')
            return redirect('add_parking')




class ReservationsListView(ListView):
    model = Customer
    template_name = 'admin_templates/dashboard.html'
    context_object_name = 'reservations'


class ParkingListView(ListView):
    model = Parking
    template_name = 'admin_templates/parking.html'




def customer_view(request,reservation_id):
    customer = get_object_or_404(Customer,id = reservation_id)
    return render(request,'admin_templates/customer_details.html',locals())

# the sequeces of the Parking Objects are yet to fixed
def update_parking(request):
    if request.method == 'POST':
        parking1 = request.POST['parking1'];            
        Parking.objects.filter(pk=1).update(reserved=Parking.objects.get(id=1).reserved+int(parking1));
        Parking.objects.filter(pk=1).update(available=Parking.objects.get(id=1).total-Parking.objects.get(id=1).reserved);

        parking2 = request.POST['parking2'];            
        Parking.objects.filter(pk=2).update(reserved=Parking.objects.get(id=2).reserved+int(parking2));
        Parking.objects.filter(pk=2).update(available=Parking.objects.get(id=2).total-Parking.objects.get(id=2).reserved);

        parking3 = request.POST['parking3'];            
        Parking.objects.filter(pk=3).update(reserved=Parking.objects.get(id=3).reserved+int(parking3));
        Parking.objects.filter(pk=3).update(available=Parking.objects.get(id=3).total-Parking.objects.get(id=3).reserved);

        parking4 = request.POST['parking4'];            
        Parking.objects.filter(pk=4).update(reserved=Parking.objects.get(id=4).reserved+int(parking4));
        Parking.objects.filter(pk=4).update(available=Parking.objects.get(id=4).total-Parking.objects.get(id=4).reserved);

        parking5 = request.POST['parking5'];            
        Parking.objects.filter(pk=5).update(reserved=Parking.objects.get(id=5).reserved+int(parking5));
        Parking.objects.filter(pk=5).update(available=Parking.objects.get(id=5).total-Parking.objects.get(id=5).reserved);

        parking6 = request.POST['parking6'];            
        Parking.objects.filter(pk=6).update(reserved=Parking.objects.get(id=6).reserved+int(parking6));
        Parking.objects.filter(pk=6).update(available=Parking.objects.get(id=6).total-Parking.objects.get(id=6).reserved);


        return HttpResponse('Success')
        
        
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