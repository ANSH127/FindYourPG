from django.contrib import admin
from django.urls import path,include
from PG import views

urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('register/',views.register,name="register"),
    path('login/',views.handlelogin,name="login"),
    path('signup/',views.handlesignup,name="signup"),
    path('logout/',views.handlelogout,name="logout"),
]
