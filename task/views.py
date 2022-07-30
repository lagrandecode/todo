from multiprocessing import context
from django.shortcuts import render
from .models import TaskModel
from .forms import *

# Create your views here.

def task_view(request):
    modelobj = TaskModel.objects.all()
    form = TaskForm()
    
    context ={
        'modelobj' : modelobj,
        'form' : form

    }
    return render(request,"home.html", context)


def task_edit(request,pk):
    editobj = TaskModel.objects.get(pk=pk)
    context = {
        'editobj':editobj
    }
    return render(request,"edit.html",context)