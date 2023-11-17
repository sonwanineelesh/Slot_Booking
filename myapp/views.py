from django.shortcuts import loader, render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world.")

def about(request):
    return HttpResponse("About page")

def service(request):
    return HttpResponse("service page")

def home(request):
    template = loader.get_template("./home.html")
    context = {
        "title": "Home Page",
        
    }
    return HttpResponse(template.render(context, request))

def userlogin(request):
    template = loader.get_template("./userlogin.html")
    context = {
        "title": "Login Page",
        "heading": "Please Login"
    }
    return HttpResponse(template.render(context, request))

def signup(request):
    template = loader.get_template("./user_signup.html")
    context = {
        "title": "Sign Up Page",
        
    }
    return HttpResponse(template.render(context, request))


def forgot_pass(request):
    template = loader.get_template("./forgot_pass.html")
    context = {
        "title": "Forgot Password Page",
        
    }
    return HttpResponse(template.render(context, request))
        