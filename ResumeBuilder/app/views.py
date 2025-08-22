from django.shortcuts import render

import os

# Create your views here.
def index(request):
    logedin = request.user.is_authenticated
    username = request.user.username
    return render(request , "home.html" , {"logedin" : logedin , "username" : username , "url" : os.environ.get("URL")})