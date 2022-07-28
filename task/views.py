from django.shortcuts import render
from .models import TaskModel

# Create your views here.

def task_view(request):
    modelobj = TaskModel.objects.all()
    context ={
        'modelobj' : modelobj

    }
    return render(request,"home.html", context)
