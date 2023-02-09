from django.shortcuts import render, redirect
from website.models import ContactModel
from website.forms import ContactForm

def index(request):
    return render(request, 'website/index.html')

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


