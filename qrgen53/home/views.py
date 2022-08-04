from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'home/index.html')

def contact_view(request):
    return render(request, 'home/contact.html')

def about_view(request):
    return render(request, 'home/about.html')
