from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/abouthistory.html')

def contact(request):
    return render(request, 'main/contact.html')

def gallery(request):
    return render(request, 'main/gallery.html')

def gamesports(request):
    return render(request, 'main/gamesports.html')

def clubsandactivities(request):
    return render(request, 'main/clubsandactivities.html')

def events(request):
    return render(request, 'main/events.html')

def schooladmin(request):
    return render(request, 'main/schooladmin.html')

def unebperformance(request):
    return render(request, 'main/unebperformance.html')

def beststudents(request):
    return render(request, 'main/beststudents.html')

def admissions(request):
    return render(request, 'main/admissions.html')