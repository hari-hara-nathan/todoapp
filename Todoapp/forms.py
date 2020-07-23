from django import forms
from .models import Todo

class Todoform(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['todo_item','lastdate']
        widgets = {
            'todo_item' : forms.TextInput(attrs={'placeholder':'enter the work','label':''}),
            'lastdate': forms.DateInput(attrs={'placeholder':'enter the lastdate'})
        }
