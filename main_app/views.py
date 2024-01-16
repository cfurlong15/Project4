from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

projects = [
    {'name': 'Project 4', 'start_date': '1/12/2024', 'end_date': '1/22/2024', 'description': 'Create project management app and successfully graduate.'},
    {'name': 'Portfolio', 'start_date': '1/1/2024', 'end_date': '1/23/2024', 'description': 'Build an amazing portfolio to show off all your great work.'},

]

def home(request):
    return render(request, 'home.html')

def projects_index(request):
    return render(request, 'projects/index.html', {
        'projects': projects
    })

def signup(request):
    error_message = ''
    if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This adds the user to the database
            user = form.save()
            # This is how we log a user in
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
            # A bad POST or GET request, so render signup.html with empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

# def logout_view(request):
#     logout(request)