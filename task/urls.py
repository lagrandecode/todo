from django.urls import path
from . import views

urlpatterns = [
    path('',views.task_view, name="home"),
    path('add/<int:pk>/',views.task_edit,)
]
