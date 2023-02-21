
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from website.models import ContactModel
from website.forms import ContactForm
from website.models import BookingModel
from website.forms import BookingForm
from website.forms import ProductModel
from website.forms import ProductForm

def index(request):
    return render(request, 'website/index.html')

def signup(request):
    if request.method == "POST":
        # username = request.POST.get('username')
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request,"Your Account has been successfully created." )

        return redirect('signin')

    return render(request, "website/signup.html")



def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "website/index.html",{'fname': fname} )

        else:
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

def addbooking(request):
    data = BookingModel.objects.all()
    print(data)
    context = {'data' : data}
    return render(request, 'website/addbooking.html', context)

def showcontact(request):
    data = ContactModel.objects.all()
    print(data)
    context = {'data' : data}
    return render(request, 'website/showcontact.html', context)


def UpdateContact(request, id):
    data = ContactModel.objects.get(id = id)
    form = ContactForm(instance=data)

    if request.method == "POST":
        form = ContactForm(request.POST, instance=data)
        print(form)
        if form.is_valid():
            form.save()
            print("Form Saved")
            return redirect("/")
        else:
            print("Form Error: ", form.errors)
    context = {'form': form}
    return render(request, 'website/update.html', context)

def Deletecontact(request, id):
    data = ContactModel.objects.get(id = id)
    data.delete()
    return redirect('showcontact')

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
    return render(request, 'website/product.html', context)

def showproduct(request):
    data = ProductModel.objects.all()
    print(data)
    context = {'data': data}
    return render (request,'website/showproduct.html', context)

def Flats(request):
    data = ProductModel.objects.filter(category=1)
    print(data)
    context = {'data': data}
    return render (request,'website/flats.html', context)

def Shoes(request):
    data = ProductModel.objects.filter(category=1)
    print(data)
    context = {'data': data}
    return render (request,'website/shoes.html', context)

def heels(request):
    data = ProductModel.objects.filter(category=1)
    print(data)
    context = {'data': data}
    return render (request,'website/heels.html', context)

def search_view(request):
    query = request.GET.get('q')
    queryset = MyModel.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    context = {'queryset': queryset, 'query': query}
    return render(request, 'search.html', context)




