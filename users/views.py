from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from . import forms

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    else:
        return render(request, "users/index.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("main:index"))
        else:
            return render(request, "users/login.html", {
                "message": "Invalid credentials."
            })
    return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("main:index"))


def new_user(request):
    if request.method == "POST":
        form = forms.NewUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            first = form.cleaned_data["first"]
            last = form.cleaned_data["last"]
            email = form.cleaned_data["email"]
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = first
            user.last_name = last
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse("main:index"))
        else:
            return render(request, "users/new.html", {
                "form": forms.NewUserForm(request.POST)
            })
    return render(request, "users/new.html", {
        "form": forms.NewUserForm()
    })