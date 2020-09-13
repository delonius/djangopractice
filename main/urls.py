from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.index, name="index"),
    path("invalid/", views.invalid, name="invalid"),
    path("404/", views.not_found, name="not_found"),
]