from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignupForm
from .models import User
from django.db.models import Q

def loginPage(request):
    context = {}
    return render(request, 'login.html', context)

def home(request):
    
    # Фильрация поиска
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    users = User.objects.filter(
        Q(first_name__icontains=q) |
        Q(last_name__icontains=q) |
        Q(parent_name__icontains=q)
        )
    
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()

    context = {'users': users, 'form': form}
    return render(request, 'admin/users.html', context)

def statistics(request):
    context = {}
    return render(request, 'admin/statistics.html', context)

def configuration(request):
    context = {}
    return render(request, 'admin/configuration.html', context)