from django import forms
from .models import Task
from django.contrib.auth.models import User

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['email', 'username','password']