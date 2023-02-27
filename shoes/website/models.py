from django.db import models
from django.contrib.auth.models import User

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

    cat = models.ForeignKey("CategoryModel", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class AddToCartModel(models.Model):
    item = models.ForeignKey(ProductModel, on_delete=models.CASCADE)    
    # name = models.CharField(max_length=50)
    # price = models.IntegerField()

    quantity = models.IntegerField(default=1)
    size = models.IntegerField()
    fit = models.CharField(max_length=15)
    # total_price = models.IntegerFielord(default=1)
    foruser = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class CartBookingModel(models.Model):
    name = models.CharField(max_length=75)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField()
    datentime = models.DateTimeField()
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=50)
    total_payment = models.CharField(max_length=20)
    services = models.JSONField(default=list)
    size = models.JSONField(default=list)
    price = models.JSONField(default=list)
    fit = models.JSONField(default=list)
    foruser = models.ForeignKey(User, on_delete=models.CASCADE)
    BookingTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    review = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return self.name