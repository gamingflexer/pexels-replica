from django.shortcuts import render
from django.http import HttpResponse
from pyunsplash import PyUnsplash

# Create your views here.

YOUR_KEY = "7dfHhkHblHq8JtO2x0u5pHaEDiY2u1yTiUAD2IUcnjo"
pu = PyUnsplash(api_key=YOUR_KEY)

def homePage(request):
    return render(request, "home.html")

def explore(request):
    search = (request.GET['search'])
    data = []
    search = pu.search(type_='photos', query=search)
    for photo in search.entries:
        data.append(photo.link_download)
    return render(request, 'explore.html', {'data': data}) 


# def explore(request):

#     return render(request, "explore.html")

def login(request):

    return render(request, "login.html")

def signup(request):

    return render(request, "signup.html")

def feedback(request):

    return render(request, "feedback.html")
