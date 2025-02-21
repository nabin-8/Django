from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from django.shortcuts import redirect, get_object_or_404

def addTask(request):
    task = request.POST.get("task")
    Task.objects.create(task=task)
    return redirect("home")


def mark_as_done(request, pk):
    # task = Task.objects.get(pk=pk)
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect("home")


def mark_as_undone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect("home")


def edit_task(request):
    task_id = request.POST.get("task_id")
    task_edit = request.POST.get("task_edit")
    task = get_object_or_404(Task, pk=task_id)
    task.task = task_edit
    task.save()
    return redirect("home")


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect("home")