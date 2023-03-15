from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta


class BookingModel(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField()
    price = models.IntegerField()
    product = models.CharField(max_length=50)
    contact = models.ForeignKey("ContactModel", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class ContactModel(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    # username = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=6)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.fname

class CategoryModel(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField()

    def __str__(self):
        return self.name
    
class ProductModel(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    img = models.ImageField()
    img2 = models.ImageField()
    img3 = models.ImageField()
    img4 = models.ImageField()
    img5 = models.ImageField()
    img6 = models.ImageField()
    desc = models.TextField()
    cat = models.ForeignKey("CategoryModel", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class AddToCartModel(models.Model):
    item = models.ForeignKey(ProductModel, on_delete=models.CASCADE)    
    # name = models.CharField(max_length=50)
    # price = models.IntegerField()
    time = models.DateField(auto_now_add=True)
    quantity = models.IntegerField(default=1)
    size = models.IntegerField()
    fit = models.CharField(max_length=15)
    total_price = models.IntegerField(default=1)
    dod = models.DateField(null=True, blank=True)
    foruser = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.item)
    

class CartBookingModel(models.Model):
    name = models.CharField(max_length=75)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField()
    datentime = models.DateField()
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=50)
    total_payment = models.CharField(max_length=20)
    services = models.JSONField(default=list)
    quantity = models.JSONField(default=list)
    size = models.JSONField(default=list)
    price = models.JSONField(default=list)
    fit = models.JSONField(default=list)
    foruser = models.ForeignKey(User, on_delete=models.CASCADE)
    BookingTime = models.DateTimeField(auto_now_add=True)
    # OrderStatus = models.CharField(max_length=15)
    description= models.CharField(max_length=500)
    dateofdelivery = models.DateField()
    order_status = models.CharField(default="Active", max_length=30)
    
    def __str__(self):
        return self.name


class TrackOrder(models.Model):
    order = models.ForeignKey(CartBookingModel, on_delete=models.CASCADE)
    # dispatch = models.CharField()

class Review(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    review = models.TextField()
    rating = models.IntegerField()
    prod = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    datentime = models.DateTimeField(auto_now_add=True)
    foruser = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class CustomUser(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password1 = models.CharField(max_length=100)
    dod = models.DateField()
    password2 = models.CharField(max_length=100)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100, blank=True, null=True)
    contact1 = models.IntegerField()
    contact2 = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.IntegerField()
    


    def __str__(self):
        return self.fname
    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)  