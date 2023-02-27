from django.shortcuts import render, redirect
from website.models import CartBookingModel
import json
from django.contrib.auth.decorators import login_required

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