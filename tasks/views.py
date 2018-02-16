from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

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


def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.time_published = timezone.now()
            task.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm()
        return render(request, 'tasks/create_task.html', {'form': form})


def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task})


def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.time_edited = timezone.now()
            task.save()
            return redirect('task_detail', pk=task.pk)
    else:
        return render(request, 'tasks/edit_task.html', {'task': task})


def delete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('home')


def delete_all(request):
    Task.objects.all().delete()
    return redirect('home')
