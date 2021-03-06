from django.urls import path
from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add, name="add"),
    path("<int:task_id>", views.view_task, name="task"),
    path("delete/<int:task_id>", views.delete_task, name="delete"),
]