from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        ordering = ['created_at']
        fields = ['title', 'completed']