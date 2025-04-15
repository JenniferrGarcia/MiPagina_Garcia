from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render, redirect
from .forms import CreateNewTask, CreateNewProject

# Create your views here.
def index(request):
    title = 'Django Course!'
    return render(request, 'index.html', {
        'title': title
    })

def about(request):
    return render(request, 'about.html')

def hello(request, username):
    return HttpResponse("Hello %s" % username)

def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {
        'projects': projects
    })

def tasks(request):
    # task = get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })

def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
        'form': CreateNewTask()})
    else:
        Task.objects.create(title=request.POST['title'],description=request.POST['description'], project_id=2)
        return redirect('/tasks/')

def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
        'form': CreateNewProject()
    })
    else:
        Project.objects.create(name=request.POST["name"])
        return render(request, 'projects/create_project.html', {
        'form': CreateNewProject()
    })