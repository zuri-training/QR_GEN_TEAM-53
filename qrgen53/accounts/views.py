from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login  # logout, urls


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
    """context = {
        'username': 'username',
        'password': 'password1'
    }"""
    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def login_view(request):
    if request.method == "POST":
        # TODO: fix the login
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is None:
            return redirect('login')  # raise error message
        else:
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('dashboard-main')

    return render(request, 'accounts/login.html')


"""form =
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']


            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')"""


def dashboard_view(request):
    username = request.user
    context = {
        'username': username
    }
    return render(request, "profile/dashboard-main.html", context)
