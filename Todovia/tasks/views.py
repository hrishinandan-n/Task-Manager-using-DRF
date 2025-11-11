from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import TaskForm
from .models import TaskInfo

# Create your views here.

@login_required(login_url='users:loginUser')
def home(request):
    """Render home page for logged-in user."""
    return render(request, 'home.html')

@login_required(login_url='users:loginUser')
def listTask(request):
    """List all tasks belonging to the current user."""
    tasks = TaskInfo.objects.filter(user=request.user)
    return render(request, 'listTask.html', {'taskList': tasks})

@login_required(login_url='users:loginUser')
def addTask(request):
    """Create a new task for the current user."""
    form = TaskForm(request.POST or None)
    if form.is_valid():
        task = form.save(commit=False)
        task.user = request.user
        task.save()
        return redirect('tasks:listTask')
    return render(request, 'addTask.html', {'form': form})

@login_required(login_url='users:loginUser')
def editTask(request, pk):
    """Edit an existing task."""
    task = get_object_or_404(TaskInfo, pk=pk, user=request.user)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('tasks:listTask')
    return render(request, 'editTask.html', {'form': form})

@login_required(login_url='users:loginUser')
def deleteTask(request, pk):
    """Delete a specific task."""
    task = get_object_or_404(TaskInfo, pk=pk, user=request.user)
    task.delete()
    return redirect('tasks:listTask')
