
from django import forms
from .models import Problem

class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ['full_name', 'college', 'department', 'problem_title', 'image', 'comment']
