from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Task
from .serializer import TaskSerializer

class TaskViewsSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

def home(request):
    return HttpResponse("Bem vindo ao Task Manager")
