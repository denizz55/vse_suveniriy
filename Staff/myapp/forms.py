from .models import Task
from django.forms import ModelForm, TextInput

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["name", "place", "price", "square"]
        widgets ={
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            "place": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Расположение'
            }),
            "price": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена'
            }),
            "square": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Площадь'
            }),
        }