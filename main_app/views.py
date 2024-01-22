from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login
from .forms import SignUpForm, TaskForm
from .models import Project, Task
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def home(request):
    return render(request, 'home.html')

def projects_index(request):
    projects = Project.objects.filter(user=request.user)
    return render(request, 'projects/index.html', {
        'projects': projects
    })

def projects_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    task_form = TaskForm()
    return render(request, 'projects/detail.html', {
        'project': project,
        'task_form': task_form
    })

def add_task(request, project_id):
    form = TaskForm(request.POST)
    if form.is_valid():
        new_task = form.save(commit=False)
        new_task.project_id = project_id
        new_task.save()
    return redirect('detail', project_id =project_id) 


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # Use the custom SignUpForm that includes first name and last name fields
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    else:
        
        form = SignUpForm()

    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


class ProjectCreate(CreateView):
    model = Project
    fields = ['name', 'description', 'start_date', 'end_date', 'status']

    def form_valid(self, form):
    
        form.instance.user = self.request.user  
        return super().form_valid(form)

class ProjectUpdate(UpdateView):
    model = Project
    fields = ['name', 'description', 'start_date', 'end_date', 'status']

class ProjectDelete(DeleteView):
    model = Project
    success_url = '/projects'

class TaskUpdate(UpdateView):
    model = Task
    fields = ['description', 'start_date', 'end_date', 'status']

    def get_success_url(self):
        project_id = self.kwargs.get('project_id')
        print(project_id, 'print project id')
        return reverse('detail', kwargs={'project_id': project_id})

def tasks_delete(request, project_id, task_id):
    project = get_object_or_404(Project, pk=project_id)
    task = get_object_or_404(Task, pk=task_id, project=project)

    if request.method == 'POST':
        task.delete()
        return redirect('detail', project_id=project_id)
    
    return render(request, 'main_app/task_confirm_delete.html', {'project': project, 'task': task})
    
    
