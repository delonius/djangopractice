from django.shortcuts import render
from django.apps import apps
Task = apps.get_model('tasks', 'Task')

# Create your views here.


def tasks_due(request):
    return len(Task.objects.filter(user=request.user).all()) if request.user.is_authenticated else None


def index(request):
    return render(request, 'main/index.html', {
        "message": None,
        "tasks_due": tasks_due(request),
    })


def invalid(request):
    return render(request, 'main/index.html', {
        "message": "Invalid credentials.",
        "tasks_due": tasks_due(request),
    })


def not_found(request):
    return render(request, "main/404.html", {
        "tasks_due": tasks_due(request),
    })
