from django.contrib import admin
from website.models import ContactModel
from website.models import BookingModel 
from website.models import ProductModel
from website.models import CategoryModel, AddToCartModel, CartBookingModel, CustomUser


admin.site.register(ContactModel)
admin.site.register(BookingModel)
admin.site.register(ProductModel)
admin.site.register(CategoryModel)
admin.site.register(AddToCartModel)
admin.site.register(CartBookingModel)
admin.site.register(CustomUser)
