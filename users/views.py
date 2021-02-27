from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from orders.models import Order


def login_page(request):
    return render(request, "users/login.html")


def login_action(request):
    username = request.POST["username"]
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is None:
        return HttpResponse("no user by this username and password")
    login(request, user)
    return redirect("main_page")


def profile_page(request):
    user = request.user
    orders = Order.objects.filter(user=user)
    d = {
        "orders": orders,
    }
    return render(request, "users/profile.html", context=d)
