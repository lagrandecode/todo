from dataclasses import fields
from django.forms import ModelForm
from .models import *

class TaskForm(ModelForm):
    class Meta:
        model = TaskModel
        fields = '__all__'