from django.contrib import admin
from website.models import ContactModel
from website.models import BookingModel 
from website.models import ProductModel


admin.site.register(ContactModel)
admin.site.register(BookingModel)
admin.site.register(ProductModel)



