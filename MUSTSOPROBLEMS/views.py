from django.shortcuts import render, redirect
from .forms import ProblemForm # type: ignore

def aboutus(request):
    if request == 'POST':
        form = ProblemForm(request.POST, request.FILES)
        if form.is_valid():

            return redirect('home')
        else: 
            form = ProblemForm()
        
        return render(request, 'home.html', {'form': form})
    
def home(request):
    if request == 'POST':
        form = ProblemForm(request.POST, request.FILES)
        if form.is_valid():

            return redirect('home')
        else:
            form = ProblemForm()
    
    return render(request,'home.html', {'form': form})

def index(request):
    if request == 'POST':
        form = ProblemForm(request.POST, request.FILES)
        if form.is_valid():

            return redirect('home')
        else:
            form = ProblemForm()
    
    return render(request,'home.html', {'form': form})