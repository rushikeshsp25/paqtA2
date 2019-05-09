from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import AddTaskForm,UserForm
from .models import Task

@login_required
def index(request):
    tasks=Task.objects.filter(added_by=request.user).order_by('-datetime')
    return render(request,'todo/index.html',{'tasks':tasks})

def loginUser(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('todo:index')
            else:
                return render(request, 'todo/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'todo/login.html', {'error_message': 'Invalid Username or password'})
    else:
        return render(request,'todo/login.html')

@login_required
def logoutUser(request):
    logout(request)
    return redirect('todo:loginUser')

def createNewUser(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            login(request, user)
            return redirect('todo:index')
    else:
        form=UserForm()
        return render(request, 'todo/signup.html', {'form':form})

@login_required
def AddTask(request):
    if request.method=="POST":
        form=AddTaskForm(request.POST)
        if form.is_valid():
            task=form.save(commit=False)
            task.added_by=request.user
            task.save()
            return redirect('todo:index')
    else:
        form=AddTaskForm()
        return render(request,'todo/add_task.html',{'form':form})


@login_required
def EditTask(request,id):
    task = get_object_or_404(Task, pk=id)
    if request.method=="POST":
        form=AddTaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('todo:index')
    else:
        form = AddTaskForm(request.POST or None, instance=task)
        return render(request,'todo/add_task.html',{'form':form})

@login_required
def DeleteTask(request,id):
    task=Task.objects.get(pk=id)
    task.delete()
    return redirect('todo:index')

@login_required
def MarkComplete(request,id):
    task=Task.objects.get(pk=id)
    task.status=True
    task.save()
    return redirect('todo:index')