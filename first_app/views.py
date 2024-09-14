from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    # return HttpResponse("Hello, Welcome to Django app")
    infos=[{
        "name": "Anurag Shimpi",
        "designation": "Data Scientist",
        "age": "22",
        "mobile": "1234567890"
    },
    {
        "name": "omkar khese",
        "designation": "Data Engineer",
        "age": "23",
        "mobile": "0987654321"
    }]
    return render(request, 'home.html', context= {'infos' : infos})

def about(request):
    context={
        "name": "Anurag Shimpi",
        "designation": "Data Scientist",
        "age": "22",
        "mobile": "1234567890"
    }
    return render(request, 'about.html', context)

def contactus(request):
    return render(request, 'contactus.html')

def services(request):
    return render(request, 'services.html')