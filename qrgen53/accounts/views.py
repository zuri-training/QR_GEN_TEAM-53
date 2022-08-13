from django.contrib.auth import authenticate, login, urls, logout, urls
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


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
    context = {'form': form}
    return render(request, 'register.html', context)


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

    return render(request, 'login.html')


def forgot_password_view(request):
    return render(request, 'forgot-password.html')


def new_password_view(request):
    return render(request, 'new-password.html')


def recover_password_view(request):
    return render(request, 'recover-password.html')


@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return render(request, 'index.html')


"""form =
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']


            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')"""



