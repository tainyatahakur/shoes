from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from website.models import ContactModel
from website.forms import ContactForm
from website.models import BookingModel
from website.forms import BookingForm
from website.forms import ProductModel
from website.forms import ProductForm
from website.forms import CategoryForm
from website.forms import CategoryModel
from website.models import AddToCartModel,CartBookingModel
from website.forms import AddToCartForm, CartBookingForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from website.forms import CreateUserForm
import json
from django.core.mail import send_mail
from shoes.settings import EMAIL_HOST_USER



def index(request):
    return render(request, 'website/index.html')

def signup(request):
    form = CreateUserForm()

    username = request.POST.get('username')
    email = request.POST.get('email')
    password1 = request.POST.get('pass1')
    password2 = request.POST.get('pass2')
    print(username)
    print(email)

    if request.method=='POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            print("Form Saved")
            user = form.cleaned_data.get("username")
            messages.success(request, "Account created for "+ user+ " succesfully")
            # response = JsonResponse({"success":True})
            return redirect("/")

        else:
            print("Invalid Form", form.errors)
            response = JsonResponse({"error":form.errors})
            response.status_code = 403
            return response

    return render(request, "website/signup.html")



def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        print('username: ', username)
        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            print("login Done")
            if request.user.is_superuser:
                return redirect('dashboard')
            return redirect('index')
        else:
           print('form error ')
           messages.error(request, "Bad Credentials")
           return redirect('index')

    return render(request, "website/signin.html")



def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('index')


def contact(request):
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            print("Form Saved")
            return redirect("/")
        else:
            print("Form Error: ", form.errors)
    context = {'form': form}
    return render(request, 'website/contact.html', context)


def booking(request):
    form = BookingForm()

    if request.method == "POST":
        form = BookingForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            print("Form Saved")
            return redirect("/")
        else:
            print("Form Error: ", form.errors)
    context = {'form': form}
    return render(request, 'website/booking.html', context)


@login_required
def addbooking(request):
    data = BookingModel.objects.all()
    print(data)
    context = {'data' : data}
    return render(request, 'website/addbooking.html', context)


@login_required
def showcontact(request):
    data = ContactModel.objects.all()
    print(data)
    context = {'data' : data}
    return render(request, 'AdminPanel/showcontact.html', context)


@login_required
def UpdateContact(request, id):
    data = ContactModel.objects.get(id = id)
    form = ContactForm(instance=data)

@login_required
def UpdateProduct(request, id):
    data = ProductModel.objects.get(id = id)

    form = ProductForm(instance=data)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=data)
        print(form)
        if form.is_valid():
            form.save()
            print("Form Saved")
            # return redirect("/")
        else:
            print("Form Error: ", form.errors)
    context = {'form': form, 'data': data}
    return render(request, 'AdminPanel/updateproduct.html', context)

@login_required
def UpdateCategory(request, id):
    data = CategoryModel.objects.get(id = id)

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
    data = ContactModel.objects.get(id = id)
    data.delete()
    return redirect('showcontact')

@login_required
def DeleteProduct(request, id):
    data = ProductModel.objects.get(id = id)
    data.delete()
    return redirect('showproduct')

@login_required
def DeleteCategory(request, id):
    data = CategoryModel.objects.get(id = id)
    data.delete()
    return redirect('showcategory')

@login_required
def product(request):
    form = ProductForm()

    if request.method == "POST":
        form = ProductForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            print("Form Saved")
            return redirect("/")
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
            return redirect("/")
        else:                                           
            print("Form Error: ", form.errors)
    context = {'form': form}
    return render(request, 'website/category.html', context)


@login_required
def showcategory(request):
    data = CategoryModel.objects.all()
    print(data)
    context = {'data': data}
    return render (request,'AdminPanel/show_prod_cat.html', context)


@login_required
def showproduct(request):
    data = ProductModel.objects.all()
    print(data)
    context = {'data': data}
    return render (request,'AdminPanel/Show_Product.html', context)



def Flats(request):
    data = ProductModel.objects.filter(cat=8)
    print(data)
    context = {'data': data}
    return render (request,'website/flats.html', context)

def Shoes(request):
    data = ProductModel.objects.filter(cat=7)
    print(data) 
    context = {'data': data}
    return render (request,'website/shoes.html', context)

def Heels(request):
    data = ProductModel.objects.filter(cat=6)
    print(data)
    context = {'data': data}
    return render (request,'website/heels.html', context)

def Boots(request):
    data = ProductModel.objects.filter(cat=15)
    print(data)
    context = {'data': data}
    return render (request,'website/boots.html', context)

def Loafer(request):
    data = ProductModel.objects.filter(cat=14)
    print(data)
    context = {'data': data}
    return render (request,'website/loafer.html', context)

def Mules(request):
    data = ProductModel.objects.filter(cat=10)
    print(data)
    context = {'data': data}
    return render (request,'website/mules.html', context)

def Pumps(request):
    data = ProductModel.objects.filter(cat=12)
    print(data)
    context = {'data': data}
    return render (request,'website/pumps.html', context)

def Sandal(request):
    data = ProductModel.objects.filter(cat=13)
    print(data)
    context = {'data': data}
    return render (request,'website/sandal.html', context)

def Sneaker(request):
    data = ProductModel.objects.filter(cat=11)
    print(data)
    context = {'data': data}
    return render (request,'website/sneaker.html', context)

def Wedges(request):
    data = ProductModel.objects.filter(cat=9)
    print(data)
    context = {'data': data}
    return render (request,'website/wedges.html', context)

def Espadrilles(request):
    data = ProductModel.objects.filter(cat=16)
    print(data)
    context = {'data': data}
    return render (request,'website/espadrilles.html', context)


@csrf_exempt
def AddToCartItem(request):
  
    data = AddToCartModel.objects.all()
    total_price = 0
    form = AddToCartForm()

    if request.method == "POST":
        print('form: ', request.POST)

        form = AddToCartForm(request.POST)
        name = request.POST.get('name')
        price = request.POST.get('price')
        userid = request.POST.get('foruser')
        foruser = User.objects.get(id=userid)
        quantity = request.POST.get('quantity')

        print("name: ", name)

        cart = AddToCartModel(name=name,price=price,quantity=quantity,foruser=foruser)
        cart.save()
        print('value')
        # if form.is_valid():
        #     form.save()
        #     return redirect("/")
        # else:
        #     print("Form Error: ", form.errors)
    # return render (request,'website/checkout.html', context)
    return JsonResponse({'amount' : name}, status=200)


@login_required
def DelCartBooking(request, id):
    item = AddToCartModel.objects.get(id=id)
    item.delete()
    print("Item Deleted")
    return redirect('checkout')
    

@login_required
def showAddToCart(request):
    data = AddToCartModel.objects.all()
    total_price = data.aggregate(Sum('price'))['price__sum']
    form = AddToCartForm()

    if request.method == "POST":
        form = AddToCartForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            form.save()
            return redirect("/")
        else:
            print("Form Error: ", form.errors)

    context = {'form': form, 'data': data, 'total_price': total_price}
    return render(request, '/showaddtocart.html', context)


@login_required
def CartAndBooking(request):
    # allitems = AddToCartModel.objects.all()
    form = CartBookingForm()
    # lenofcart = len(allitems)
    s = 0
    items = AddToCartModel.objects.filter(foruser = request.user.id)
    for i in items:
        s += i.price

    if request.method == "POST":
        form = CartBookingForm(request.POST)
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        someuser = request.POST.get('foruser')
        foruser = User.objects.get(id=someuser)
        datentime = request.POST.get('datentime')
        se = request.POST.getlist('services')
        total_payment = request.POST.get('total_payment')
        services = json.dumps(se)
        print("Services: ", services)
        print("name: ", name)
        print("Services: ", phone)
        print("Services: ", email)
        print("Services: ", foruser)
        print("Services: ", datentime)
        print("Services: ", total_payment)

        print("Services: ", services)
        booking = CartBookingModel(name=name,phone=phone, email=email, datentime=datentime, total_payment=total_payment, services=services, foruser=foruser)
        booking.save()
        print("Value Saved")

    context = {'item':items, 'total': s}
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
    data = CartBookingModel.objects.all()
    context = {'data': data}
    return render(request, 'AdminPanel/userbooking.html', context)