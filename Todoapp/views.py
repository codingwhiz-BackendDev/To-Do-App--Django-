from django.shortcuts import render, redirect
from .models import Todo
from django.contrib import messages
# Create your views here.

def index(request):
    todos = Todo.objects.all()
    if request.method == 'POST':
        title = request.POST['title']
        if title != '':
            new_todo = Todo.objects.create(title=title)
            new_todo.save();
        else:
            messages.info(request, 'Please input something')
            return redirect('/')
        
            
    return render(request, 'index.html',{'todos':todos})

def delete(request, id):
    todos = Todo.objects.get(id=id)
    todos.delete()
    return redirect('/')