from django.urls import path,include
from website import views
from . import views


urlpatterns = [

    path('', views.index, name="index" ),
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
    path('updatecategory/<int:id>/', views.UpdateCategory, name = 'updatecategory'),
    path('delete/<int:id>/', views.Deletecontact, name = 'delete' ),
    path('deleteproduct/<int:id>/', views.DeleteProduct, name = 'deleteproduct' ),
    path('deletecategory/<int:id>/', views.DeleteCategory, name = 'deletecatgory' ),
    path('addtocart/', views.AddToCartItem, name = 'AddToCart'),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    path('Checkout/', views.CartAndBooking, name="checkout"),
    path('UserCart/', views.DelAllBooking, name="usercart"),
    path('DetailProduct/<int:id>/', views.detailproduct, name="DetailProduct"),
    path('CategoryWiseProducts/<int:id>/', views.ProductsCatviewPage, name="CategoryWiseProducts"),
    path('review/', views.review, name='review'),
    path('Search/', views.search, name ='Search'),
    
    path('delcartitem/<int:id>/', views.DelCartBooking, name="delcartbooking"),

]