from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from .form import CreateUserForm
from django.contrib.auth.decorators import login_required
from .form import *
from .models import *
# Create your views here.


def index(request):
    tasks = Task.objects.filter(user=request.user)
    
    form = TaskForm()
    
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
        return redirect('list')
    
    context = {'tasks':tasks, 'form':form}
    return render(request, 'tasks/list.html', context)

def updateTask(request,pk):
    task = Task.objects.get(id=pk)  
    form = TaskForm(instance=task)
    
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('list')
    
    context = {'form':form}
    
    return render(request, 'tasks/update_task.html', context)
    
def deleteTask(request,pk):
    item = Task.objects.get(id=pk)
    
    if request.method == "POST":
        item.delete()
        return redirect('list')
    
    context = {'item':item}
    return render(request, 'tasks/delete.html', context)

def loginpage(request):  
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return render(request, 'tasks/loginpage.html', {"message": "Username OR paswword is incorrect"})
    return render(request, 'tasks/loginpage.html')
    
def logoutuser(request):
    logout(request)
    return redirect('loginpage')
    

def registeruser(request):
    form = CreateUserForm()
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginpage')
            
    context = {'form':form}
    return render(request, 'tasks/registeruser.html', context)
    
    

    