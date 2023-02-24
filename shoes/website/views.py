
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
from website.models import AddToCartModel
from website.forms import AddToCartForm

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
        pass1 = request.POST['password']
        print('username: ', username)
        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            print("login Done")
            # return render(request, "website/index.html",{'fname': fname} )
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
    return render(request, 'AdminPanel/contact.html', context)

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
    return render(request, 'AdminPanel/showcontact.html', context)


def UpdateContact(request, id):
    data = ContactModel.objects.get(id = id)
    form = ContactForm(instance=data)

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

def Deletecontact(request, id):
    data = ContactModel.objects.get(id = id)
    data.delete()
    return redirect('showcontact')

def DeleteProduct(request, id):
    data = ProductModel.objects.get(id = id)
    data.delete()
    return redirect('showproduct')

def DeleteCategory(request, id):
    data = CategoryModel.objects.get(id = id)
    data.delete()
    return redirect('showcategory')

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

def showcategory(request):
    data = CategoryModel.objects.all()
    print(data)
    context = {'data': data}
    return render (request,'AdminPanel/show_prod_cat.html', context)

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

def AddToCart(request):
    data = AddToCartModel.objects.all()
    total_price = 0
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
    return render(request, 'website/checkoutpage.html', context)

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




