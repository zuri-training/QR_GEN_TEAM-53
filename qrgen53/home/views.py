from django.shortcuts import render


# Create your views here.
def home_view(request):
    return render(request, 'index.html')


def contact_view(request):
    return render(request, 'contact.html')


def about_view(request):
    return render(request, 'about.html')


def privacy_policy_view(request):
    return render(request, 'privacy-policy.html')


def faq_view(request):
    return render(request, 'faq.html')


def tos_view(request):
    return render(request, 'tos.html')
