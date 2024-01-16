from django.shortcuts import render

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