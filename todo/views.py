from django.shortcuts import render, redirect
from django.contrib import messages

# importing of todo form and models
from .forms import TodoForm
from .models import appTodo

# Indexing all of data todolist
def index(request):
    item_list = appTodo.objects.order_by("-created_at")

    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('index')
    form = TodoForm()

    pageup = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }

    return render(request, 'index.html', {'form':form,})


# function that deletes an item uses the primary key todo item id from the url.
def remove(request, item_id):
    item = appTodo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "The item has been deleted !!!")

    return redirect('index')