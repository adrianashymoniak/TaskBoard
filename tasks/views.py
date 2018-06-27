from datetime import datetime

from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import SignUpForm, TaskForm
from .models import Task


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'tasks/signup.html', {'form': form})


@login_required(login_url='login/')
def home(request):
    user = request.user
    tasks = Task.objects.filter(user=user).order_by('time_published')
    return render(request, 'tasks/home_page.html', {'tasks': tasks})


@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.time_published = datetime.now()
            task.status = 'New'
            task.save()
            return redirect('task_detail', pk=task.pk)
        else:
            task = Task()
            task.priorities = request.POST["priorities"]
            task.task_title = request.POST["task_title"]
            task.task_description = request.POST["task_description"]
            estimated = request.POST['time_estimated']
            if estimated:
                task.time_estimated = datetime.strptime(estimated, '%Y-%m-%d').date()
            else:
                task.time_estimated = estimated
            return render(request, 'tasks/create_task.html', {'form': form, 'task': task})
    else:
        form = TaskForm()
        return render(request, 'tasks/create_task.html', {'form': form})


@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task})


@login_required
def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.time_edited = datetime.now()
            task.save()
            return redirect('task_detail', pk=task.pk)
        else:
            task.status = request.POST['status']
            task.priorities = request.POST['priorities']
            task.task_title = request.POST['task_title']
            task.task_description = request.POST['task_description']
            estimated = request.POST['time_estimated']
            if estimated:
                task.time_estimated = datetime.strptime(estimated, '%Y-%m-%d').date()
            else:
                task.time_estimated = estimated
            return render(request, 'tasks/edit_task.html', {'form': form, 'task': task})
    else:
        return render(request, 'tasks/edit_task.html', {'task': task})


@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if task:
        task.delete()
        return redirect('home')
    else:
        return error_404(request, None)


@login_required
def delete_all(request):
    Task.objects.filter(user_id=request.user).delete()
    return redirect('home')


def error_404(request, exception):
    data = {}
    return render(request, 'tasks/errors/404.html', data)


def error_500(request):
    data = {}
    return render(request, 'tasks/errors/500.html', data)
