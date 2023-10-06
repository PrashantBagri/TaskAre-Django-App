from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import newUser, Task
from .forms import taskForm, userRegister
from django.db.models import Q
from django.contrib import messages
from datetime import date

# Create your views here.

def taskCompleted(request, pk):
    task = Task.objects.get(id=pk)
    task.isCompleted = True
    task.save()
    return redirect('home')

@login_required(login_url='login')
def taskare(request):
    createdBy = request.user
    # task = Task.objects.all()
    form = taskForm()
    today = date.today()
    if request.method == 'POST':
        form = taskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            if task.targetDate > today:
                task.createdBy = request.user
                task.save()
                return redirect('home')
            else:
                messages.error(request, "Invalid Date")
        
    tasks = Task.objects.filter(createdBy=createdBy)
        
    context = {'form' : form, "createdBy": createdBy, "tasks":tasks}
    return render(request, 'base/home.html' , context)

@login_required(login_url='login')
def taskPage(request, pk):
    task = Task.objects.get(id=pk)
    context = {"task": task}
    return render(request, 'base/Task.html', context)

@login_required(login_url='login')
def editTask(request, pk):  
    task = Task.objects.get(id = pk)
    form = taskForm(instance = task)
    if request.method == "POST":
        form = taskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task', task.id)
    context = {"form":form}
    return render(request, 'base/edit.html', context)

@login_required(login_url='login')
def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == "POST":
        task.delete()
        return redirect('home')
    context={"task" : task}
    return render(request, 'base/taskDelete.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = newUser.objects.filter(username = username)

        if not user.exists():
            messages.error(request, "Invalid Username")
            return redirect('login')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Error.Try Again.")
        
                    
    context={}
    return render(request, 'base/login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = userRegister(label_suffix='')
    if request.method == "POST":
        form = userRegister(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.set_password(user.password)
            user.save()
            login(request, user)
            return redirect('home')
    context={"form":form}
    return render(request, 'base/register_new.html', context)

