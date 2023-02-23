from django.urls import path,include
# from AdminPanel import views
from website import views
# from . import views


urlpatterns = [

    # path('', views.index ),
    path('product/', views.product, name='product'),
    path('showproduct/', views.showproduct, name ='showproduct'),
    path('category/', views.category, name='Category'),
    path('showcategory/', views.showcategory, name ='showcategory'),    
]



