from django import forms

# importing the modules
from .models import appTodo

class TodoForm(forms.ModelForm):
    class Meta:
        model = appTodo
        fields = '__all__'