from audioop import reverse
from multiprocessing import context
from django.shortcuts import render, redirect
from .models import TaskModel
from .forms import *

# Create your views here.

def task_view(request):
    modelobj = TaskModel.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
            'modelobj': modelobj,
            'form': form
        }
    return render(request, "home.html", context)



def task_edit(request,pk):
    editobj = TaskModel.objects.get(pk=pk)
    updateform = TaskForm(instance=editobj)
    if request.method == "POST":
        updateform = TaskForm(request.POST, instance=editobj)
        if updateform.is_valid():
            updateform.save()
            return redirect('/')
    context = {
        'editobj': editobj,
        'updateform': updateform
    }
    return render(request,"edit.html",context)


#passing delete functio into the todo 
def task_delete(request,pk):
    deleteobj = TaskModel.objects.get(pk=pk)
    deleteobj.delete()
    return redirect('/')
   