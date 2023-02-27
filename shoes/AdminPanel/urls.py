from django.urls import path,include
from AdminPanel.views import dashboard, ViewuserBooking
from website import views



urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('product/', views.product, name='product'),
    path('showproduct/', views.showproduct, name ='showproduct'),
    path('category/', views.category, name='Category'),
    path('showcategory/', views.showcategory, name ='showcategory'),
    path('showcontact/', views.showcontact, name='showcontact'),
    path('showBookings/', views.ShowUserBookings, name='showbooking'),
    path('ViewUserBookings/<int:id>/', ViewuserBooking, name='viewuserbooking'),

]



