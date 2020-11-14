from django.shortcuts import render

def auth_home(request):
    return render(request,"auth_home.html")


def auth_login(request):
    return render(request,"auth_login.html")


def auth_register(request):
    return render(request,"auth_register.html")