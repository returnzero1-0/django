from django.urls import path
from . import views

urlpatterns=[

    path('',views.auth_home,name='auth_home'),
    path(r'auth_login/',views.auth_login,name='auth_login'),
    path(r'auth_register/',views.auth_register,name='auth_register'),
    
   

]