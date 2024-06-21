
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ProblemForm

def home(request):
    if request.method == 'POST':
        form = ProblemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Form submitted successfully')
    else:
        form = ProblemForm()
    return render(request, 'home.html', {'form': form})
