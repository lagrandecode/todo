from django.urls import path
from . import views

urlpatterns = [
    path('',views.task_view, name="home"),
    path('edit/<int:pk>/',views.task_edit),
    path('delete/<int:pk>/',views.task_delete),
    
]
