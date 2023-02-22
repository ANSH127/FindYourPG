from django.contrib import admin
from django.urls import path,include
from PG import views

urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('register/',views.register,name="register"),
    path('booking/',views.booking,name="booking"),
    path('login/',views.handlelogin,name="login"),
    path('signup/',views.handlesignup,name="signup"),
    path('logout/',views.handlelogout,name="logout"),
    path('forget_password/',views.forget_password,name="forget_password"),
    path('change_password/<str:token>/',views.change_password,name="change_password"),
    path('<int:myid>/handleduepayment',views.handleduepayment,name="handleduepayment"),
    path('<str:slug>/<int:myid>/<str:slug2>',views.view,name="view"),
    path('<str:slug>/<int:myid>/<str:slug2>/checkout',views.checkout,name="checkout"),
    path('<str:slug>/<int:myid>/<str:slug2>/schedule',views.schedule,name="schedule"),
    path('<str:slug>/<int:myid>/<str:slug2>/handlepayment',views.handlepayment,name="payment"),
    path('check/<int:myid>',views.check,name="check"),
    path('<str:slug>/',views.home1,name="home1"),
]
