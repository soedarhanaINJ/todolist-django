from django.shortcuts import render, redirect
from django.contrib import messages

# importing of todo form and models
from .forms import TodoForm
from .models import appTodo

# Indexing all of data todolist
def index(request):
    item_list = appTodo.objects.order_by("-created_at")

    form = TodoForm()

    pageup = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }

    return render(request, 'index.html', pageup)


# function that deletes an item uses the primary key todo item id from the url.
def remove(request, item_id):
    item = appTodo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "The item has been deleted !!!")

    return redirect('index')

# Create or add some todo on FE (frontend)
def addtodo_view(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('todo_list')
    else:
        form = TodoForm()

    return render(request, 'crud/create.html', {'form': form})

# CRUD part R (Read), showing all of data or value of list
def todolist_view(request):
    todos = appTodo.objects.order_by("-created_at")

    return render(request, 'crud/todo_list.html', {"todos": todos})