from django.urls import path
from website import views


urlpatterns = [
    path('', views.index ),
    path('contact/', views.contact, name='contact'),
    path('showcontact/', views.showcontact, name = 'showcontact'),
    path('update/<int:id>/', views.UpdateContact, name = 'update'),
    path('delete/<int:id>/', views.Deletecontact, name = 'delete' )
]