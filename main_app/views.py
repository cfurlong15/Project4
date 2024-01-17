from django.shortcuts import render, redirect
from django.contrib.auth import login
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from .models import Project
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from .forms import ProfileForm

# Create your views here.

# projects = [
#     {'name': 'Project 4', 'start_date': '1/12/2024', 'end_date': '1/22/2024', 'description': 'Create project management app and successfully graduate.'},
#     {'name': 'Portfolio', 'start_date': '1/1/2024', 'end_date': '1/23/2024', 'description': 'Build an amazing portfolio to show off all your great work.'},
# ]

def home(request):
    return render(request, 'home.html')

def projects_index(request):
    projects = Project.objects.filter(user=request.user)
    # projects = Project.objects.all()
    return render(request, 'projects/index.html', {
        'projects': projects
    })

def projects_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    return render(request, 'projects/detail.html', {
        'project': project
    })


# def signup(request):
#     error_message = ''
#     if request.method == 'POST':
#     # This is how to create a 'user' form object
#     # that includes the data from the browser
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             # This adds the user to the database
#             user = form.save()
#             # This is how we log a user in
#             login(request, user)
#             return redirect('index')
#         else:
#             error_message = 'Invalid sign up - try again'
#             # A bad POST or GET request, so render signup.html with empty form
#     # form = UserCreationForm()
#     form = UserCreationForm()
#     context = {'form': form, 'error_message': error_message}
#     return render(request, 'registration/signup.html', context)


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # Use the custom SignUpForm that includes first name and last name fields
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # Load the profile instance created by the signal
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    else:
        # Use the custom SignUpForm for GET requests
        form = SignUpForm()

    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


class ProjectCreate(CreateView):
    model = Project
    fields = ['name', 'description', 'start_date', 'end_date', 'status']

    def form_valid(self, form):
    # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
        return super().form_valid(form)

class ProjectUpdate(UpdateView):
    model = Project
    fields = ['name', 'description', 'start_date', 'end_date', 'status']

class ProjectDelete(DeleteView):
    model = Project
    success_url = '/projects'