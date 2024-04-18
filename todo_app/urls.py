from django.urls import path 
from . import views
urlpatterns = [
    path("", views.TodoList.as_view(), name="todo-list"),
    path("create-todo/", views.CreateTodo.as_view(), name="create-todo"),
    path("todo/<int:pk>/", views.TodoDetail.as_view(), name="detail-todo"),
    path("todo-update/<int:pk>", views.TodoUpdate.as_view(), name="todo-update"),
    path("todo-delete/<int:pk>", views.TodoDelete.as_view(), name="todo-delete"),
]