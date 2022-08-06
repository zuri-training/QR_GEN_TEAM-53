from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # TODO: handle user already exists error
        if form.is_valid():
            form.validate_unique()
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

        print("out")
    form = UserCreationForm()
    context = {
        'username': 'username',
        'password': 'password1'
    }
    return render(request, 'accounts/register.html', context)


def login_view(request):
    return render(request, 'accounts/login.html')


def dashboard_view(request):
    username = request.user
    context = {}
    return render(request, "profile/dashboard.html", {})
