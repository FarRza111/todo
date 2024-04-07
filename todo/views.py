from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from django.shortcuts import redirect, get_object_or_404


# Create your views here.
def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk = pk)
    task.is_completed = True
    task.save()
    return redirect('home')


