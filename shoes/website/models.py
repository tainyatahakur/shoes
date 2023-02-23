from django.db import models

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
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

class CategoryModel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class ProductModel(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    cat = models.ForeignKey("CategoryModel", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class AddToCartModel(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)
    total_price = models.IntegerField(default=1)

    def _str_(self):
        return self.name
