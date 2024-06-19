from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'todos', views.AppTodoView, 'todo')

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<str:item_id>', views.remove, name='remove'),
    path('add/todo/', views.addtodo_view, name='addtodo_view'),
    path('view/', views.todolist_view, name='todo_list'),

    path('api/', include(router.urls)),
]