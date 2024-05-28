from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('delete/<str:item_id>', views.remove, name='remove'),
    path('add/', views.addtodolist, name='addtodo'),
]
