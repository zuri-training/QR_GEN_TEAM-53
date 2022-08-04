from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

"""
def index(request):
    return render(request, 'accounts/index.html')
"""

def register_view(request):
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
    return render(request, 'accounts/register.html', context)


def login_view(request):
    return render(request, 'accounts/login.html')

def dashboard_view(request):
    return render(request, "profile/dashboard.html",{})