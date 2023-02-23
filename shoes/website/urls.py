from django.urls import path,include
from website import views
from . import views


urlpatterns = [

    path('', views.index ),
    path('contact/', views.contact, name='contact'),
    path('booking/', views.booking, name ='booking'),
    path('showcontact/', views.showcontact, name = 'showcontact'),
    path('showbooking/', views.addbooking, name = 'showbooking'),
    path('heels/', views.Heels, name = 'heels'),
    path('shoes/', views.Shoes, name = 'shoes'),
    path('flats/', views.Flats, name = 'flats'),
    path('boots/', views.Boots, name = 'boots'),
    path('loafer/', views.Loafer, name = 'loafer'),
    path('mules/', views.Mules, name = 'mules'),
    path('pumps/', views.Pumps, name= 'pumps'),
    path('sandal/', views.Sandal, name = 'sandal'),
    path('sneaker/', views.Sneaker, name = 'sneaker'),
    path('wedges/', views.Wedges, name = 'wedges'),
    path('espadrilles', views.Espadrilles, name = 'espadrilles'),
    path('update/<int:id>/', views.UpdateContact, name = 'update'),
    path('updateproduct/<int:id>/', views.UpdateProduct, name = 'updateproduct'),
    path('delete/<int:id>/', views.Deletecontact, name = 'delete' ),
    path('deleteproduct/<int:id>/', views.DeleteProduct, name = 'deleteproduct' ),
    path('addtocart/', views.AddToCart, name = 'AddToCart'),
    path('', views.index, name="index"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),


]