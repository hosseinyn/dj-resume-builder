from django.shortcuts import render , redirect , get_object_or_404

from django.contrib.auth.decorators import login_required

from .models import Resume
from .forms import CreateResume

from time import sleep

# Create your views here.
@login_required
def create_resume(request):
    if request.method == "GET":
        logedin = request.user.is_authenticated
        username = request.user.username
        form = CreateResume()
        return render(request , "create_resume.html" , {"logedin" : logedin , "username" : username , "form" : form})
    
    elif request.method == "POST":
        form = CreateResume(request.POST , request.FILES)
        if form.is_valid():
            profile = form.cleaned_data["profile_picture"]
            full_name = form.cleaned_data["full_name"]
            birthday = form.cleaned_data["birthday"]
            email = form.cleaned_data["email"]
            phone = form.cleaned_data["phone"]
            skills = form.cleaned_data["skills"]
            school = form.cleaned_data["school"]
            degree = form.cleaned_data["degree"]
            job_title = form.cleaned_data["job_title"]
            company = form.cleaned_data["company"]
            job_start_date = form.cleaned_data["job_start_date"]
            job_end_date = form.cleaned_data["job_end_date"]

            Resume.objects.create(user = request.user ,profile_picture = profile , full_name = full_name , birthday = birthday , email = email , phone = phone , skills = skills , school = school , degree = degree , job_title = job_title , job_start_date = job_start_date , job_end_date = job_end_date)
            # form.save()
            return redirect("/account/panel")
        else:
            return redirect("/")
        

@login_required
def delete_resume(request , access_id):
    if get_object_or_404(Resume , access_id=access_id).user == request.user:
        Resume.objects.get(access_id=access_id).delete()
        return redirect("/account/panel")
    else:
        return redirect("/account/login")

@login_required
def edit_resume(request , access_id):
    user_resume = Resume.objects.get(access_id = access_id)
    if get_object_or_404(Resume , access_id = access_id).user == request.user:
        if request.method == "GET":
            form = CreateResume(instance=user_resume)

            logedin = request.user.is_authenticated
            username = request.user.username

            return render(request , "edit_resume.html" , {"logedin" : logedin , "username" : username , "form" : form , "access_id" : access_id})
        
        elif request.method == "POST":
            form = CreateResume(request.POST , request.FILES , instance=user_resume)
            
            if form.is_valid():
                cd = form.cleaned_data
                user_resume.profile_picture = cd["profile_picture"]
                user_resume.full_name = cd["full_name"]
                user_resume.birthday = cd["birthday"]
                user_resume.email = cd["email"]
                user_resume.phone = cd["phone"]
                user_resume.skills = cd["skills"]
                user_resume.school = cd["school"]
                user_resume.degree = cd["degree"]
                user_resume.job_title = cd["job_title"]
                user_resume.company = cd["company"]
                user_resume.job_start_date = cd["job_start_date"]
                user_resume.job_end_date = cd["job_end_date"]
                user_resume.user = request.user

                user_resume.save()
            
                return redirect("/account/panel")
            
            else:
                return redirect("/account/panel")
    else:
        return redirect("/account/login")
    

def resume(request , access_id):
    target_resume = get_object_or_404(Resume , access_id=access_id)

    logedin = request.user.is_authenticated
    username = request.user.username

    return render(request , "resume.html" , {"logedin" : logedin , "username" : username , "resume" : target_resume})