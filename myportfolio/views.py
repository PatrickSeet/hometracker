from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")

def aboutme(request):
    return render(request, "about_me.html")

def projects(request):
    return render(request, "projects.html")