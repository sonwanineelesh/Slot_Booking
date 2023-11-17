from django.urls import path
from django.contrib import admin
from myapp import views

urlpatterns = [
    
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("service", views.service, name="service"),
    path("home", views.home, name="home"),
    path("userlogin", views.userlogin, name="userlogin"),
    path("user_signup", views.signup, name="signup"),
    path("forgot_pass", views.forgot_pass, name="forgot_pass"),
]