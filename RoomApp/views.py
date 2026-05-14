from django.shortcuts import render,redirect
from .models import  Room
from hostelapp.models import hostel

# Create your views here.

def Add_room(request):


    if request.method == 'POST':

        hostel_id = request.POST.get('hostel')
        room_number = request.POST.get('room_number')
        capacity = request.POST.get('capacity')
        beds = request.POST.get('beds')
        price = request.POST.get('price')
        image1 = request.FILES.get('image1')
        image2 = request.FILES.get('image2')

        Hostel = hostel.objects.get(id=hostel_id)

        Room.objects.create(
            hostel=Hostel,
            room_number=room_number,
            capacity=capacity,
            available_beds=beds,
            price_per_month=price,
            image1 = image1,
            image2 = image2
        )
        return redirect('Room_page')

def update_room(request, room_id):

    room = Room.objects.get(id=room_id)

    if request.method == "POST":

        hostel_id = request.POST.get('hostel')
        room_number = request.POST.get('room_number')
        capacity = request.POST.get('capacity')
        beds = request.POST.get('beds')
        price = request.POST.get('price')

        room.room_number = room_number
        room.capacity = capacity
        room.available_beds = beds
        room.price_per_month = price

        if request.FILES.get('image1'):
            room.image1 = request.FILES.get('image1')

        if request.FILES.get('image2'):
            room.image2 = request.FILES.get('image2')

        room.save()

        return redirect('View_Room')

def delete_room(request, room_id):

    room = Room.objects.get(id=room_id)
    room.delete()

    return redirect('View_Room')






