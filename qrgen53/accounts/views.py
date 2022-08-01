from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login


def index(request):
    return render(request, 'accounts/index.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')

    else:
        form = UserCreationForm()

    form = UserCreationForm()
    context = {'form': form}
    return render(request, 'registration/register.html', context)
"""
def login(request):
    form = 
    context = {'form': form}
    return render(request, 'registration/login.html', context)
"""
