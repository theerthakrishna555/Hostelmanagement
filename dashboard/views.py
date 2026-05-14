from django.shortcuts import render
from hostelapp.views import *
from hostelapp.models import *
from RoomApp.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def dashboard(request):
    if request.user.role == 'student':
        return render(request,'dashboard/student.html')
    elif request.user.role == 'warden':

        return render(request,'dashboard/warden_side/warden.html')
    elif request.user.role == 'admin' or request.user.is_superuser:
        return render(request,'dashboard/admin_side/admin.html')

def add_hostel(request):
    return render(request,'dashboard/warden_side/add_hostel.html')

def view_hostel_page(request):
    warden_hostel = hostel.objects.filter(warden=request.user)
    return render(request,'dashboard/warden_side/view_hostel.html',{'warden_hostel':warden_hostel})

def admin_hostel_page(request):
    admin_hostel = hostel.objects.all()
    return render(request,'dashboard/admin_side/admin_hostel.html',{'admin_hostel':admin_hostel})

@login_required
def approve_hostel(request, hostel_id):

    if not request.user.is_superuser:
        return redirect("home")

    hostel_approve = hostel.objects.get(id=hostel_id)

    hostel_approve.is_Approved = True
    hostel_approve.save()

    return redirect("admin_hostel_page")

def Room_page(request):
    hostel_list = hostel.objects.filter(warden=request.user,is_Approved=True)
    return render(request,'dashboard/warden_side/add_room.html',{'hostel_list':hostel_list})


def View_Room(request):
    hostel_list = hostel.objects.filter(warden=request.user)

    if not hostel_list.exists():
        return redirect('add_hostel')

    room_list = Room.objects.filter(hostel__warden=request.user)

    return render(request, 'dashboard/warden_side/view_room.html', {
        'room_list': room_list
    })

def Edit_room(request,room_id):
    room_data = Room.objects.get(id=room_id)
    return render(request, 'dashboard/warden_side/Edit_room.html', {'room_data':room_data})

def Edit_hostel(request,hostel_id):
    hostel_data = hostel.objects.get(id=hostel_id)
    return render(request,'dashboard/warden_side/Edit_hostel.html',{'hostel_data':hostel_data})

