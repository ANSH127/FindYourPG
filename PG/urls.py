from django.contrib import admin
from django.urls import path,include
from PG import views

urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('register/',views.register,name="register"),
    path('<str:slug>/<int:myid>/<str:slug2>',views.view,name="view"),
    path('<str:slug>/<int:myid>/<str:slug2>/checkout',views.checkout,name="checkout"),
    path('<str:slug>/<int:myid>/<str:slug2>/schedule',views.schedule,name="schedule"),
    path('<str:slug>/<int:myid>/<str:slug2>/handlepayment',views.handlepayment,name="payment"),
    path('<str:slug>/',views.home1,name="home1"),
    path('login/',views.handlelogin,name="login"),
    path('signup/',views.handlesignup,name="signup"),
    path('logout/',views.handlelogout,name="logout"),
]
