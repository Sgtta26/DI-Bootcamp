from django.shortcuts import render
from .models import Category, Todo
from .forms import TodoForm

# Create your views here.

def add_todo(request):

    # GET
    todo_form = TodoForm()

    # POST
    if request.method == 'POST':

        todo_form_filled = TodoForm(request.POST)
        todo_form_filled.save()

    context = {'form': todo_form}
    return render(request, 'add_todo.html', context)


def all_todos(request):
    todos = Todo.objects.all()

    context = {'todos': todos}
    return render(request, 'todo_list.html', context)

