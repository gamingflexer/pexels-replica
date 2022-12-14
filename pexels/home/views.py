from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from pyunsplash import PyUnsplash
from .serializers import FileSerializer
from rest_framework.views import APIView
import requests
from home.keys import unsplash_key
from home.forms import PostForm


# Create your views here.

pu = PyUnsplash(api_key=unsplash_key)

def temp(request):
    return render(request, "home.html")

def homePage(request):
    return render(request, "home.html")

def explore(request):
    try:
        try:
            search = (request.GET['search'])
        except KeyError:
            search = "nature"
        data = []
        search = pu.search(type_='photos', query=search)
        for photo in search.entries:
            data.append(photo.link_download)
        return render(request, 'explore.html', {'data': data}) 
    except requests.exceptions.ConnectionError:
        return render(request, 'explore.html', {'data': "No Internet Connection!!"})
        
def feedback(request):

    return render(request, "feedback.html")

def aboutus(request):

    return render(request, "aboutus.html")

def upload(request):
    return render(request, "upload.html")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('home')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('home')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('home')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('home')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('home')
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = True
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!!")
        
    return render(request, "signup.html")


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            # messages.success(request, "Logged In Sucessfully!!")
            return render(request, "index.html",{"fname":fname})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('home')
    
    return render(request, "login.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('home')


class FileView(APIView):  # for getting REPORT upload
    parser_classes = (MultiPartParser, FormParser)

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            pathOfFile = file_serializer.data['file']
        else:
            return Response(file_serializer.errors['file'], status=status.HTTP_400_BAD_REQUEST)
        
def feedback2(request):
 
    # check if the request is post
    if request.method =='POST': 
 
        # Pass the form data to the form class
        details = PostForm(request.POST)
 
        # In the 'form' class the clean function
        # is defined, if all the data is correct
        # as per the clean function, it returns true
        if details.is_valid(): 
 
            # Temporarily make an object to be add some
            # logic into the data if there is such a need
            # before writing to the database  
            post = details.save(commit = False)
 
            # Finally write the changes into database
            post.save() 
 
            # redirect it to some another page indicating data
            # was inserted successfully
            return HttpResponse("data submitted successfully")
             
        else:
         
            # Redirect back to the same page if the data
            # was invalid
            return render(request, "feedback2.html", {'form':details}) 
    else:
 
        # If the request is a GET request then,
        # create an empty form object and
        # render it into the page
        form = PostForm(None)  
        return render(request, 'feedback2.html', {'form':form})
