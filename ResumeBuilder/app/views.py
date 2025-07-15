from django.shortcuts import render

# Create your views here.
def index(request):
    logedin = request.user.is_authenticated
    username = request.user.username
    return render(request , "home.html" , {"logedin" : logedin , "username" : username})