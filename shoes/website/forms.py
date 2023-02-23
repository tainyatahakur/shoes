from django.forms import ModelForm
from website.models import ContactModel
from website.models import BookingModel
from website.models import ProductModel 
from website.models import CategoryModel
from website.models import AddToCartModel

class ContactForm(ModelForm):
    class Meta:
        model = ContactModel
        fields = "__all__"

class BookingForm(ModelForm):
    class Meta:
        model = BookingModel
        fields = "__all__"

class ProductForm(ModelForm):
    class Meta:
        model = ProductModel
        fields = "__all__" 

class CategoryForm(ModelForm):
    class Meta:
        model = CategoryModel
        fields = "__all__"        

class AddToCartForm(ModelForm):
    class Meta:
        model = AddToCartModel
        fields = "__all__"