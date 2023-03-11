from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from website.models import ContactModel
from website.forms import ContactForm
from website.models import BookingModel
from website.forms import BookingForm
from django.utils import timezone
from website.forms import ProductModel
from website.forms import ProductForm
from website.forms import CategoryForm
from website.forms import CategoryModel
from website.models import AddToCartModel, CartBookingModel, CustomUser
from website.forms import AddToCartForm, CartBookingForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from website.forms import CreateUserForm, CustomUserForm
import json            
import random         

from django.core.mail import send_mail
from shoes.settings import EMAIL_HOST_USER
from website.forms import ReviewForm
from django.core import serializers
from website.models import Review
from datetime import date, timedelta
from website.models import Order


def index(request):
    data = ProductModel.objects.all()[:9]
    item = ProductModel.objects.all()[:4]
    navs = CategoryModel.objects.all()
    if request.user.is_authenticated:
        cart = AddToCartModel.objects.filter(foruser=request.user)
        lenofcart = len(cart)
    else:
        lenofcart = 0
    print("Len of cart; ", lenofcart)

    if request.method == "POST":
        search = request.POST.get('search')
        print("Searchindex: ", search)
        # query = request.POST.get('search')
        if search:
            data = ProductModel.objects.filter(cat__name__icontains=search)
            print("data: ", data)
            return render(request, 'website/search.html', {'data': data})
        else:
            print("Not Found")

    context = {'data': data, 'item': item,
               'navs': navs, 'lenofcart': lenofcart}
    return render(request, 'website/index.html', context)


def ProductsCatviewPage(request, id):
    if request.user.is_authenticated:
        cart = AddToCartModel.objects.filter(foruser=request.user)
        lenofcart = len(cart)
    else:
        lenofcart = 0
    print("Len of cart; ", lenofcart)
    navs = CategoryModel.objects.all()
    catid = CategoryModel.objects.get(id=id)
    data = ProductModel.objects.filter(cat=catid)
    context = {'catid': catid, 'navs': navs,
               'data': data, 'lenofcart': lenofcart}
    return render(request, 'website/productcatviewpage.html', context)


def signup(request):
    form = CreateUserForm()
    customform = CustomUserForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        contact1 = request.POST.get('contact1')
        contact2 = request.POST.get('contact2')
        dod = request.POST.get('dod')
        print("Dod: ", dod)
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        otp = request.POST.get('otp')
        print('otp', otp)
        print('username: ', username)
        user = authenticate(email=email, password=password1, passwors=password2, address1=address1,dod=dod,
                            address2=address2, contact1=contact1, contact2=contact2, city=city, state=state, zip=zip)

        form = CreateUserForm(request.POST)
        customform = CustomUserForm(request.POST)
        print(customform)
        if form.is_valid():
            if customform.is_valid():
                random_numbers = random.randint(111111, 999999)
                print("Signup Done")
                send_mail("User Data: ", f"OTP: {random_numbers}", EMAIL_HOST_USER, [
                  email  ], fail_silently=True)
                messages.success(
                    request, 'OTP sent successfully on your registered email')
                user = form.save()
                customform.save()
                login(request, user)
                print("Form2 save")
                return render(request, 'website/verification.html', {"otp": random_numbers})
            else:
                print("Form2 Error: ", customform.errors)
            form.save()
            print("Form Saved")
            user = form.cleaned_data.get("username")
            messages.success(request, "Account created for " +
                             user + " successfully")
            # response = JsonResponse({"success":True})
            return redirect("/")

        else:
            print("Invalid Form", form.errors)
            messages.success(request, form.errors)

    return render(request, "website/signup.html")


def signin(request):
    if request.method == 'POST':

        email = request.POST.get('email')
        print("Email: ", email)
        pass1 = request.POST.get('password')
        print("Password: ", pass1)
        username = User.objects.get(email=email).username
        otp = request.POST.get('otp')
        print('otp', otp)
        user = authenticate(request, username=username, password=pass1)
        print("User: ", user)
        if user is not None:
            login(request, user)
            random_numbers = random.randint(111111, 999999)
            print("login Done")
            send_mail("User Data: ", f"OTP: {random_numbers}", EMAIL_HOST_USER, [email] , fail_silently=True)

            messages.success(request, 'OTP sent successfully on your registered email')
            if request.user.is_superuser:
                return redirect('dashboard')
            return render(request, 'website/verification.html', {"otp": random_numbers})
        else:
            print('form error ')
            messages.error(request, "Wrong Credentials")
        #    return redirect('index')

    return render(request, "website/signin.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('index')


def contact(request):
    form = ContactForm()
    navs = CategoryModel.objects.all()           

    if request.method == "POST":
        form = ContactForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            print("Form Saved")
            # return redirect("/")
        else:
            print("Form Error: ", form.errors)
    context = {'form': form, 'navs': navs}
    return render(request, 'website/contact.html', context)


def booking(request):
    form = BookingForm()

    if request.method == "POST":
        form = BookingForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            print("Form Saved")
            # return redirect("/")
        else:
            print("Form Error: ", form.errors)
    context = {'form': form}
    return render(request, 'website/booking.html', context)


@login_required
def addbooking(request):
    data = BookingModel.objects.all()
    print(data)
    context = {'data': data}
    return render(request, 'website/addbooking.html', context)


@login_required
def showcontact(request):
    data = ContactModel.objects.all()
    print(data)
    context = {'data': data}
    return render(request, 'AdminPanel/showcontact.html', context)


@login_required
def UpdateContact(request, id):
    data = ContactModel.objects.get(id=id)
    form = ContactForm(instance=data)


@login_required
def UpdateProduct(request, id):
    data = ProductModel.objects.get(id=id)

    form = ProductForm(instance=data)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES ,instance=data)
        print(form)
        if form.is_valid():
            form.save()
            print("Form Saved")
            messages.success(request, "product added successfully")

            # return redirect("/")
        else:
            print("Form Error: ", form.errors)
    context = {'form': form, 'data': data}
    return render(request, 'AdminPanel/updateproduct.html', context)


@login_required
def UpdateCategory(request, id):
    data = CategoryModel.objects.get(id=id)

    form = CategoryForm(instance=data)

    if request.method == "POST":
        form = CategoryForm(request.POST, instance=data)
        print(form)
        if form.is_valid():
            form.save()
            print("Form Saved")

        else:
            print("Form Error: ", form.errors)
    context = {'form': form, 'data': data}
    return render(request, 'AdminPanel/updatecategory.html', context)


@login_required
def Deletecontact(request, id):
    data = ContactModel.objects.get(id=id)
    data.delete()
    return redirect('showcontact')


@login_required
def DeleteProduct(request, id):
    data = ProductModel.objects.get(id=id)
    data.delete()
    return redirect('showproduct')


@login_required
def DeleteCategory(request, id):
    data = CategoryModel.objects.get(id=id)
    data.delete()
    return redirect('showcategory')


@login_required
def product(request):
    form = ProductForm()

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            print("Form Saved")
            messages.success(request, "product added successfully")
            # return redirect("/")
        else:
            print("Form Error: ", form.errors)
    context = {'form': form}
    return render(request, 'AdminPanel/add_product.html', context)


@login_required
def category(request):
    form = CategoryForm()

    if request.method == "POST":
        name = request.POST.get('name')
        print("Name: ", name)
        form = CategoryForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            print("Form Saved")
            messages.success(request, "ProductCategory added successfully")

            # return redirect("/")
        else:
            print("Form Error: ", form.errors)
    context = {'form': form}
    return render(request, 'website/category.html', context)


@login_required
def showcategory(request):
    data = CategoryModel.objects.all()
    print(data)
    context = {'data': data}
    return render(request, 'AdminPanel/show_prod_cat.html', context)


@login_required
def showproduct(request):
    data = ProductModel.objects.all()
    if request.method == "POST":
        search = request.POST.get('search')
        data = ProductModel.objects.filter(name__icontains=search)
        # for i in data:
        #     print(i)
    print(data)
    context = {'data': data}
    return render(request, 'AdminPanel/Show_Product.html', context)


def Flats(request):
    data = ProductModel.objects.filter(cat=8)
    print(data)
    context = {'data': data}
    return render(request, 'website/flats.html', context)


def Shoes(request):
    data = ProductModel.objects.filter(cat=7)
    print(data)
    context = {'data': data}
    return render(request, 'website/shoes.html', context)


def Heels(request):
    data = ProductModel.objects.filter(cat=6)
    print(data)
    context = {'data': data}
    return render(request, 'website/heels.html', context)


def Boots(request):
    data = ProductModel.objects.filter(cat=15)
    print(data)
    context = {'data': data}
    return render(request, 'website/boots.html', context)


def Loafer(request):
    data = ProductModel.objects.filter(cat=14)
    print(data)
    context = {'data': data}
    return render(request, 'website/loafer.html', context)


def Mules(request):
    data = ProductModel.objects.filter(cat=10)
    print(data)
    context = {'data': data}
    return render(request, 'website/mules.html', context)


def Pumps(request):
    data = ProductModel.objects.filter(cat=12)
    print(data)
    context = {'data': data}
    return render(request, 'website/pumps.html', context)


def Sandal(request):
    data = ProductModel.objects.filter(cat=13)
    print(data)
    context = {'data': data}
    return render(request, 'website/sandal.html', context)


def Sneaker(request):
    data = ProductModel.objects.filter(cat=11)
    print(data)
    context = {'data': data}
    return render(request, 'website/sneaker.html', context)


def Wedges(request):
    data = ProductModel.objects.filter(cat=9)
    print(data)
    context = {'data': data}
    return render(request, 'website/wedges.html', context)


def Espadrilles(request):
    data = ProductModel.objects.filter(cat=16)
    print(data)
    context = {'data': data}
    return render(request, 'website/espadrilles.html', context)


@csrf_exempt
def AddToCartItem(request):

    data = AddToCartModel.objects.all()
    total_price = 0
    form = AddToCartForm()

    if request.method == "POST":
        print('form: ', request.POST)

        form = AddToCartForm(request.POST)
        name = request.POST.get('item')
        item = ProductModel.objects.get(id=name)
        total_price = request.POST.get('total_price')
        fit = request.POST.get('fit')
        size = request.POST.get('size')

        print("Name: ", name, total_price, fit)
        userid = request.POST.get('foruser')
        foruser = User.objects.get(id=userid)
        quantity = request.POST.get('quantity')

        print("name: ", name)

        cart = AddToCartModel(item=item,total_price=total_price,quantity=quantity,foruser=foruser, fit=fit, size=size)
        cart.save()
        print('value')
        # if form.is_valid():
        #     form.save()
        #     # return redirect("/")
        #     print("Form Saved")
        # else:
        #     print("Form Error: ", form.errors)
    # return render (request,'website/checkout.html', context)
    return JsonResponse({'amount': name}, status=200)


@login_required
def DelCartBooking(request, id):
    item = AddToCartModel.objects.get(id=id)
    item.delete()
    print("Item Deleted")
    return redirect('checkout')


@login_required
def showAddToCart(request):
    data = AddToCartModel.objects.all()
    total_price = data.aggregate(sum('price'))['price__sum']
    form = AddToCartForm()

    if request.method == "POST":
        form = AddToCartForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            form.save()

        else:
            print("Form Error: ", form.errors)

    context = {'form': form, 'data': data, 'total_price': total_price}
    return render(request, '/showaddtocart.html', context)


@login_required
def CartAndBooking(request):
    # allitems = AddToCartModel.objects.all()
    form = CartBookingForm()
    today = date.today()
    activeuser = request.user.username
    print(activeuser)
    someuser = CustomUser.objects.get(username=activeuser)
    print("SomeUser: ",someuser)
    dod = today + timedelta(days=4)
    # lenofcart = len(allitems)
    s = 0
    items = AddToCartModel.objects.filter(foruser=request.user.id)
    for i in items:
        s += i.total_price

    if request.method == "POST":
        form = CartBookingForm(request.POST)
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        someuser = request.POST.get('foruser')
        foruser = User.objects.get(id=someuser)
        datentime = request.POST.get('datentime')
        se = request.POST.getlist('services')
        sizes = request.POST.getlist('size')
        fits = request.POST.getlist('fit')
        address = request.POST.get('address')
        city = request.POST.get('city')
        zip = request.POST.get('zip')
        state = request.POST.get('state')
        quantity = request.POST.getlist('quantity')

        prices = request.POST.getlist('price')
        orderstatus = request.POST.getlist('OrderStatus')
        
        total_payment = request.POST.get('total_payment')
        services = json.dumps(se)
        size = json.dumps(sizes)
        fit = json.dumps(fits)
        price = json.dumps(prices)

        print("Services: ", services)
        print("name: ", name)
        print("phone: ", phone)
        print("email: ", email)
        print("for user: ", foruser)
        print("datentime: ", datentime)
        print("total Payment: ", total_payment)

        booking = CartBookingModel(name=name, phone=phone, email=email, datentime=datentime,address=address, city=city, zip=zip, quantity=quantity,state=state,
                                   total_payment=total_payment, services=services, foruser=foruser, size=size, fit=fit, price=price,OrderStatus=orderstatus,dateofdelivery=dod)
        booking.save()
        print("Value Saved")
        # if form.is_valid():
        #     form.save()
        #     print("Form Saved")
        # else:
        #     print("Error: ", form.errors)
        return redirect('OrderHistory')
    context = {'item': items, 'total': s, 'today': today, 'dod': dod, 'someuser': someuser}
    return render(request, 'website/checkoutpage.html', context)


@login_required
def DelAllBooking(request):
    if request.method == "POST":
        foruser = request.POST.get('foruser')

        item = AddToCartModel.objects.filter(foruser=foruser)
        print("Item: ", item)
        for i in item:
            i.delete()
        print("All Item Deleted")
    return redirect('checkout')


@login_required
def ShowUserBookings(request):
    if request.user.is_superuser:
        data = CartBookingModel.objects.all()
        context = {'data': data}
        return render(request, 'AdminPanel/userbooking.html', context)
    else:
        navs = CategoryModel.objects.all()

        data = CartBookingModel.objects.filter(foruser=request.user)
        context = {'data': data, 'navs': navs}
        return render(request, 'website/userbooking.html', context)


def detailproduct(request, id):
    last_six_reviews = list(Review.objects.all())
    rating = last_six_reviews[-5:]
    # cart = AddToCartModel.objects.filter(foruser=request.user)
    if request.user.is_authenticated:
        cart = AddToCartModel.objects.filter(foruser=request.user)
        lenofcart = len(cart)
    else:
        lenofcart = 0
    print("Len of cart; ", lenofcart)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            print('form.saved')
    else:
        form = ReviewForm()
    navs = CategoryModel.objects.all()

    data = ProductModel.objects.get(id=id)
    context = {'data': data, 'navs': navs, 'form': form,
               'rating': rating, 'lenofcart': lenofcart}
    return render(request, 'website/detailproduct.html', context)


@csrf_exempt
def review(request):
    rating = Review.objects.all()
    if request.method == 'POST':
        form = ReviewForm(request.POST)                               
        name = request.POST.get('name')
        rating = request.POST.get('rating')
        email = request.POST.get('email')
        review = request.POST.get('review')
        prod = request.POST.get('prod')
        prodid = ProductModel.objects.get(id=prod)
        print("Data: ", name, email, rating, review, prod)

        someform = Review(name=name, rating=rating,
                          email=email, review=review, prod=prodid)
        someform.save()
        print(' Review form Saved')

        # if form.is_valid():
        #     form.save()
        #     print(' Review form Saved')
    else:
        form = ReviewForm()
    return render(request, 'website/review.html', {'form': form, 'ratings': rating})


@csrf_exempt
def search(request):
    results = ""
    search = ""

    if request.method == "POST":
        search = request.POST.get('search')
        print("Search: ", search)
        # query = request.POST.get('search')
        if search:
            searchres = CategoryModel.objects.filter(name__icontains=search)
            datas = serializers.serialize("json", searchres)
            print("res: ", results)
            return render(request, 'website/search.html', {'datas': datas})
        else:
            data = None
    context = {'results': results, 'query': search}
    # return render(request, 'home/search.html', context)
    # return render(request, 'website/search.html', context)
    # return JsonResponse(data, safe=False)
    return render(request, 'website/search.html', {'result': data})


def show_review(request):
    context = {"all_data": Review.objects.all(), }
    return render(request, "show_review.html", context)


# send_mail("User Data: ", f"Hello\nYour Email: {username}\n This is password: {password1}", EMAIL_HOST_USER, ['kumardigamberjha7@gmail.com'], fail_silently=True)

# def verification(request):
#     if request.method == "POST":
#         form = VerificationForm(request.POST)
#         if form.is_valid():
#             otp = form.save(commit=False)
#             form.save()

#         else:
#             print("Form Error: ", form.errors)

#     return render(request, 'website/verification.html')


def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print("Email: ", email)
        random_numbers = random.randint(111111, 999999)
        print("Signup Done")
        send_mail("User Data: ", f"OTP: {random_numbers}", EMAIL_HOST_USER, email , fail_silently=True)
        messages.success(request, 'OTP sent successfully on your registered email')
        return render(request, 'website/new_password.html', {'otp': random_numbers, 'email': email})

    return render(request, 'website/forgot_password.html')          


@csrf_exempt
def new_password(request):
    email = request.GET.get('email')
    print("email: ", email)
    user = User.objects.get(email=email)
    print("User: ", user)
    if request.method == 'POST':
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        print("pass1: ", pass1)
        print("pass2: ", pass2)
        if pass1 == pass2:
            user.set_password(pass2)
            user.save()
            print("Password Saved")
        # send_mail("User Data: ", f"OTP: {random_numbers}", EMAIL_HOST_USER, ['kumardigamberjha7@gmail.com'], fail_silently=True)
        messages.success(request, 'OTP sent successfully on your registered email')
        # return redirect('')

    return render(request, 'website/change_password.html')       


def record(request):
    foruser = request.user
    record = CartBookingModel.objects.filter()
    user = CartBookingModel.objects.filter(foruser= foruser)
    context = {
        'record': record,
    }
    return render(request, 'website/record.html', context)

@login_required
def order_history(request):
    foruser = request.user
    navs = CategoryModel.objects.all()

    record = CartBookingModel.objects.filter(foruser= foruser).values('id','dateofdelivery', 'BookingTime', 'description','services', 'quantity', 'size', 'price', 'fit')
    for booking in record:
        booking['services'] = json.loads(booking['services'])
        booking['quantity'] = booking['quantity']
        booking['size'] = json.loads(booking['size'])
        booking['price'] = json.loads(booking['price'])
        booking['fit'] = json.loads(booking['fit'])

    print("record: ",record)
    context = {
        'record': record, 'navs': navs
    }
    # return render(request, 'website/order_history.html', {'orders': record})
    return render(request, 'website/order_history.html', context)

# def order_history(request):
#     today = timezone.now().date()
#     date_range = [
#         (today - timedelta(days=30)).strftime('%Y-%m-%d'),
#         (today - timedelta(days=180)).strftime('%Y-%m-%d'),
#     ]
#     selected_date = request.GET.get('date', date_range[0])
#     orders = CartBookingModel.objects.filter(
#         datentime = selected_date,
#         foruser = request.user
#     ).order_by('datentime')
#     context = {
#         'date_range':date_range,
#         'selected_date':selected_date,
#         'orders':orders
#     }
#     return render(request, 'website/order_history.html', context)


# def UserProfile(request):  
#     return(request, 'website/account.html')

@login_required
def Your_profile(request):
    navs = CategoryModel.objects.all()

    context = {'navs': navs}
    return render(request, 'website/account.html', context)


@login_required
def Invoice(request, id):
    foruser = request.user
    data= CartBookingModel.objects.filter(id=id).values('id','address','dateofdelivery', 'total_payment', 'BookingTime', 'description','services', 'quantity', 'price','name', 'datentime')

    for booking in data:
        booking['services'] = json.loads(booking['services'])
        booking['price'] = json.loads(booking['price'])
        booking['quantity'] = booking['quantity']

    context = {'data': data}#, 'services': services,'price': price, 'q': quantity}
    return render(request, 'website/invoice.html', context)