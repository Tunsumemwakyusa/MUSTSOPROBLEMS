from django.shortcuts import render
from .forms import ProblemForm

def index(request):
    return render(request, 'index.html')

def home(request):
    if request.method == 'POST':
        form = ProblemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Handle successful form submission
    else:
        form = ProblemForm()
    return render(request, 'home.html', {'form': form})


def aboutus(request):
    return render(request, 'aboutus.html')

def platform(request):
    return render(request, 'platform.html')

def team(request):
    return render(request, 'team.html')

def contactus(request):
    return render(request, 'contactus.html')
