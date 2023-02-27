from django.forms import ModelForm
from website.models import ContactModel
from website.models import BookingModel
from website.models import ProductModel 
from website.models import CategoryModel
from website.models import AddToCartModel
from website.models import CartBookingModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from website.models import Review


class CreateUserForm(UserCreationForm):
    # phone_no = forms.CharField(max_length = 10)
    class Meta:
        model = User
        fields = ["username","email","password1", 'password2']

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

class CartBookingForm(ModelForm):
    class Meta:
        model = CartBookingModel
        fields = '__all__'

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'email', 'review', 'rating']