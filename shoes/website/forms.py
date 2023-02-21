from django.forms import ModelForm
from website.models import ContactModel
from website.models import BookingModel
from website.models import ProductModel

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