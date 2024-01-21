from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Task

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=100, required=True, help_text='Required.')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['description', 'start_date', 'end_date', 'status']