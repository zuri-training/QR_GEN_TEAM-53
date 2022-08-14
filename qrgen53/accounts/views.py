from django.contrib import messages  # import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail, BadHeaderError
from django.db.models.query_utils import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


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
            return redirect('dashboard-main')
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
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',  # TODO: change to domain name during production
                        'site_name': 'Website',  # TODO: change to name during production
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',  # TODO: change during production
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com', [user.email], fail_silently=False)
                    except BadHeaderError:

                        return HttpResponse('Invalid header found.')

                    messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
                    context = {'sent': True}
                    return render(request, 'forgot-password.html', context)

            messages.error(request, 'An invalid email has been entered.')
    form = PasswordResetForm()
    context = {'sent': False, "form": form}
    return render(request, 'forgot-password.html', context)


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
