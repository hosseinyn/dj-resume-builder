from django.shortcuts import render , redirect

from .forms import LoginForm , SignUpForm , ChangePasswordForm
from django.contrib.auth import login as login_user
from django.contrib.auth import logout as logout_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from resume.models import Resume

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "GET":
        form = LoginForm()
        return render(request , "auth/login.html" , {"form" : form})
    
    elif request.method == "POST":
        form = LoginForm(request=request , data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login_user(request , user)
            return redirect("/")
        else:
            return render(request , "auth/login.html" , {"form" : form})

def signup(request):
    if request.user.is_authenticated:
        return redirect("/")
    
    if request.method == "GET":
        form = SignUpForm()
        return render(request , "auth/signup.html" , {"form" : form})
    
    elif request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/account/login/")
        else:
            return render(request , "auth/signup.html" , {"form" : form})

@login_required
def panel(request):
    logedin = request.user.is_authenticated
    username = request.user.username

    resumes = Resume.objects.filter(user=request.user)

    resumes_count = len(resumes)

    return render(request , "auth/panel.html" , {"logedin" : logedin , "username" : username , "resumes" : resumes , "resumes_count" : resumes_count})

@login_required
def logout(request):
    if request.method == "POST":
        logout_user(request)
        return redirect("/")
    else:
        return redirect("/account/panel")

@login_required
def delete_account(request):
    if request.method == "POST":
        User.objects.get(username=request.user.username).delete()
        return redirect("/")
    else:
        return redirect("/account/panel")
    
@login_required
def change_password(request):
    if request.method == "GET":
        form = ChangePasswordForm(user=request.user)

        logedin = request.user.is_authenticated
        username = request.user.username

        return render(request , "auth/change_password.html" , {"logedin" : logedin , "username" : username , "form" : form})
    
    elif request.method == "POST":
        form = ChangePasswordForm(user=request.user , data=request.POST)

        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            logedin = request.user.is_authenticated
            username = request.user.username

            return render(request , "auth/change_password.html" , {"logedin" : logedin , "username" : username , "form" : form})