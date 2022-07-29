from multiprocessing import context
from django.shortcuts import render
from .models import TaskModel

# Create your views here.

def task_view(request):
    modelobj = TaskModel.objects.all()
    context ={
        'modelobj' : modelobj

    }
    return render(request,"home.html", context)


def task_edit(request,pk):
    editobj = TaskModel.objects.get(pk=pk)
    context = {
        'editobj':editobj
    }
    return render(request,"edit.html",context)