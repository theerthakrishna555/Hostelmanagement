from django.shortcuts import render,redirect
from hostelapp.models import *
from django.contrib.auth.decorators import login_required

@login_required
def add_hostel_details(request):

    if request.user.role != "warden":
        return redirect('home')



    if request.method == "POST":
        h_name = request.POST.get('name')
        h_location = request.POST.get('location')
        h_description = request.POST.get('description')
        h_image = request.FILES.get('Image')


        hostel.objects.create(
            name = h_name,
            location = h_location,
            description = h_description,
            warden = request.user,
            is_Approved = False,
            image = h_image

        )

        return redirect('dashboard')

    return  render(request,"dashboard/warden_side/add_hostel.html")


def update_hostel(request, hostel_id):

    Hostel = hostel.objects.get(id=hostel_id)

    if request.method == "POST":

        name = request.POST.get('name')
        location = request.POST.get('location')
        description = request.POST.get('description')

        Hostel.name = name
        Hostel.location = location
        Hostel.description = description

        if request.FILES.get('Image'):
            Hostel.image = request.FILES.get('Image')

        Hostel.save()
        return redirect('view_hostel')

def delete_hostel(request, hostel_id):

    hostel_obj = hostel.objects.get(id=hostel_id)

    hostel_obj.delete()

    return redirect('view_hostel')



