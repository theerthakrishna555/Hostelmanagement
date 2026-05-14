from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
import razorpay



# Create your views here.

def home_page(request):
    room_list = Room.objects.all()
    hostel_list = hostel.objects.filter(is_Approved=True)
    return render(request,'home.html',{'room_list':room_list,'hostel_list':hostel_list})

def hostel_list_page(request):
    hostel_list = hostel.objects.filter(is_Approved=True)
    return render(request,'hostels.html',{'hostel_list':hostel_list})

def search_hostel(request):
    location = request.GET.get('location')
    hostels = hostel.objects.filter(location__icontains=location)
    return render(request, 'hostels.html', {'hostels': hostels})

def Room_list_page(request,filtered_hostel_id):
    filtered_hostel_room = Room.objects.filter(hostel_id=filtered_hostel_id)
    return render(request,'Rooms.html',{'filtered_hostel_room':filtered_hostel_room})


def single_room_page(request,room_id):
    single_room = Room.objects.get(id=room_id)
    return render(request,'single_room.html',{'single_room':single_room})

def booking_page(request, room_id):
    room = Room.objects.get(id=room_id)

    beds = request.GET.get('beds')
    total = request.GET.get('total')

    if request.method == "POST":

        if not request.user.is_authenticated:
            return redirect('login')

        address = request.POST.get('address')
        phone = request.POST.get('phone')
        beds = int(request.POST.get('beds'))
        email = request.POST.get('email')
        total = request.POST.get('total')
        hostel_name = request.POST.get('hostel')
        capacity = request.POST.get('share')

        if beds > room.available_beds:
            return HttpResponse("Not enough beds available")


        booking = book_details.objects.create(
            student=request.user,
            Address=address,
            number=phone,
            email=email,
            hostel_name=hostel_name,
            share=capacity,
            Number_of_beds=beds,
            Total_price=total,
            room=room,
            is_paid=False
        )


        room.available_beds -= beds
        room.save()


        return redirect('payment_page', booking.id)

    return render(request, 'booking_page.html', {
        'room': room,
        'beds': beds,
        'total': total
    })




def payment_page(request, id):

    booking = book_details.objects.get(id=id)

    customer=booking.student
    pay= booking.Total_price
    amount=int(pay*100)
    pay_str=str(amount)

    if request.method == 'POST':
        order_currency='INR'
        client=razorpay.client(auth=('rzp_test_0ib0jPwwZ7I1lT','VjHNO5zKeKxz8PYe7VnzwxMR'))
        payment=client.order.create({
            'amount':amount,
            'currency':order_currency
        })


    return render(request, 'payment.html', {
        'booking': booking,
        'amount':amount,
        'pay_str':pay_str
    })




def About_page(request):
    return render(request,'About_us.html')

def contact_page(request):
    return render(request,'contact.html')

def all_rooms_page(request):
    all_rooms = Room.objects.all()
    return render(request,'All_rooms.html',{'all_rooms':all_rooms})

def succes_page(request, id):

    booking = book_details.objects.get(id=id)

    booking.is_paid = True
    booking.save()

    return render(request, 'sucess.html', {
        'booking': booking
    })
