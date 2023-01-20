from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from .forms import CreateNewTask, CreateNewProject

# Create your views here.
def index(request):
    title = 'Django course'
    return render(request, 'index.html', {
        'title': title
    })

def hello(request, username):
    return HttpResponse('<h1>Helo %s</h1>' % username)

def about(request):
    return render(request, 'about.html')

def projects(request):
    projects = Project.objects.all()
    print(projects)
    return render(request, 'projects.html', {
        'projects': projects
    })

def tasks(request):
    # task = Task.objects.get(id=id)
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {
        'tasks': tasks
    })

def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {
        'form': CreateNewTask()
        })    
    else:
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=2)
        return redirect('/tasks/')

def create_project(request):
    if request.method == 'GET':
        return render(request, 'create_project.html', {
        'form': CreateNewProject()
        })
    else: 
        project = Project.objects.create(name=request.POST['name'])
        print(project)
        return redirect('/projects/')