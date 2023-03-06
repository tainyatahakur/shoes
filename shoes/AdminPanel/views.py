from django.shortcuts import render, redirect
from website.models import CartBookingModel
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from website.models import CustomUser

@login_required
def dashboard(request):
    return render(request, 'AdminPanel/index.html')


@login_required
def ViewuserBooking(request, id):
    data = CartBookingModel.objects.get(id=id)
    somedata = json.loads(data.services)
    context = {'data': data, 'somedata': somedata}
    if request.user.is_superuser:
        return render(request, 'AdminPanel/viewuserbooking.html', context)
    else:
        return render(request, 'website/viewuserbookings.html', context)
    

@login_required
def ShowUserData(request):
    data = CustomUser.objects.all()

    context = {'data': data}
    return render(request, 'AdminPanel/showuserdata.html', context)


@login_required
def ViewUserData(request, id):
    data = CustomUser.objects.get(id=id)
    context = {'data': data}
    return render(request, 'AdminPanel/viewuserdata.html', context)


@login_required
def Accounts(request):
    data = CartBookingModel.objects.all()
    context = {'data': data}
    return render(request, 'AdminPanel/accounts.html', context)


@login_required
def ShowTodayBooking(request):
    return render()