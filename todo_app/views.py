from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Todo


class TodoList(ListView):
    model = Todo

class CreateTodo(CreateView):
    model = Todo
    fields = "__all__"
    success_url = reverse_lazy("todo-list")

class TodoDetail(DetailView):
    model = Todo

class TodoUpdate(UpdateView):
    model = Todo    
    fields = "__all__"
    success_url = reverse_lazy("todo-list")

class TodoDelete(DeleteView):
    model = Todo
    success_url = reverse_lazy('todo-list')
