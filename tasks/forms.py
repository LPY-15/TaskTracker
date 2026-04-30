from django import forms
from . import models

class TaskForm(forms.ModelForm):
    class Meta:
        model = models.task
        fields = ['task_name']
        widgets = {
            'task_name': forms.TextInput(attrs={'id': 'task-create-form'})
        }