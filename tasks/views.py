from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Task
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


@login_required(login_url='main:not_found')
def index(request):
    tasks = Task.objects.filter(user=request.user).all()
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })


@login_required
def add(request):
    if request.method == "POST":
        title = request.POST["title"]
        entry = request.POST["entry"]
        task = Task(user=request.user, name=title, entry=entry)
        task.save()
        return HttpResponseRedirect(reverse('tasks:index'))
    return render(request, "tasks/add.html")


@login_required
def view_task(request, task_id):
    try:
        task = Task.objects.get(pk=int(task_id))
        if not task.user == request.user:
            return HttpResponseRedirect(reverse("main:not_found"))
        else:
            return render(request, "tasks/task.html", {
                "task": task,
            })
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse("main:not_found"))


@login_required
def delete_task(request, task_id):
    task = Task.objects.get(pk=int(task_id))
    if not task.user == request.user:
        return HttpResponseRedirect(reverse("main:not_found"))
    else:
        task.delete()
        return HttpResponseRedirect(reverse('tasks:index'))
