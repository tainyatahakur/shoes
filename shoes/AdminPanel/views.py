# from django.shortcuts import render, redirect
# from website.forms import AddToCart
# from website.forms import addbooking

# def AddToCart(request):
#     data = AddToCartModel.objects.all()
#     total_price = 0
#     form = AddToCartForm()

#     if request.method == "POST":
#         form = AddToCartForm(request.POST)
#         if form.is_valid():
#             product = form.save(commit=False)
#             form.save()
#             return redirect("/")
#         else:
#             print("Form Error: ", form.errors)

#     context = {'form': form, 'data': data, 'total_price': total_price}
#     return render(request, 'website/checkoutpage.html', context)

# def showAddToCart(request):
#     data = AddToCartModel.objects.all()
#     total_price = data.aggregate(Sum('price'))['price__sum']
#     form = AddToCartForm()

#     if request.method == "POST":
#         form = AddToCartForm(request.POST)
#         if form.is_valid():
#             product = form.save(commit=False)
#             form.save()
#             return redirect("/")
#         else:
#             print("Form Error: ", form.errors)

#     context = {'form': form, 'data': data, 'total_price': total_price}
#     return render(request, 'home/showaddtocart.html', context)

# def booking(request):
#     form = BookingForm()

#     if request.method == "POST":
#         form = BookingForm(request.POST)
#         print(form)
#         if form.is_valid():
#             form.save()
#             print("Form Saved")
#             return redirect("/")
#         else:
#             print("Form Error: ", form.errors)
#     context = {'form': form}
#     return render(request, 'website/booking.html', context)

# def addbooking(request):
#     data = BookingModel.objects.all()
#     print(data)
#     context = {'data' : data}
#     return render(request, 'website/addbooking.html', context)