from django import forms
from todolist.models import Task
from django.forms import ModelForm

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('user', 'date', 'title', 'deskripsi')
        exclude = ['user', 'date']
