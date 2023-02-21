from django.urls import path,include
from website import views
from . import views


urlpatterns = [

    path('', views.index ),
    path('contact/', views.contact, name='contact'),
    path('booking/', views.booking, name ='booking'),
    path('showcontact/', views.showcontact, name = 'showcontact'),
    path('showbooking/', views.addbooking, name = 'showbooking'),
    path('product/', views.product, name='product'),
    path('showproduct/', views.showproduct, name ='showproduct'),
    path('heels/', views.heels, name = 'heels'),
    path('shoes/', views.Shoes, name = 'shoes'),
    path('flats/', views.Flats, name = 'flats'),
    path('update/<int:id>/', views.UpdateContact, name = 'update'),
    path('delete/<int:id>/', views.Deletecontact, name = 'delete' ),

    path('', views.index, name="index"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),


]