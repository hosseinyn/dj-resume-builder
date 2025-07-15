from django import forms

from .models import Resume

class CreateResume(forms.ModelForm):
        profile_picture = forms.ImageField(widget=forms.FileInput(attrs={"class" : "resume-input" ,"accept" : "image/*" , "style" : "border: 0;"}))
        full_name = forms.CharField(required=True , min_length=5 , max_length=25 , widget=forms.TextInput(attrs={"class" : "resume-input"}) , label="Full Name ")
        birthday = forms.DateField(required=True , widget=forms.DateInput(attrs={"class" : "resume-input" , "type" : "date"}) , label="Your Birthday ")
        email = forms.EmailField(required=False , widget=forms.EmailInput(attrs={"class" : "resume-input"}) , label="Your Email")
        phone = forms.IntegerField(required=False , widget=forms.NumberInput(attrs={"class" : "resume-input"}) , label="Your Phone Number")

        school = forms.CharField(required=False , max_length=30 , min_length=5 , widget=forms.TextInput(attrs={"class" : "resume-input"}) , label="School")
        degree = forms.CharField(required=False , max_length=10 , min_length=2 , widget=forms.TextInput(attrs={"class" : "resume-input"}) , label="Degree ")

        job_title = forms.CharField(required=True , max_length=15 , min_length=2 , widget=forms.TextInput(attrs={"class" : "resume-input"}) , label="Job Title ")
        company = forms.CharField(required=False , max_length=15 , min_length=2 , widget=forms.TextInput(attrs={"class" : "resume-input"}) , label="Company ")
        job_start_date = forms.DateField(required=False , widget=forms.DateInput(attrs={"class" : "resume-input" , "type" : "date"}) , label="Job Start Date ")
        job_end_date = forms.DateField(required=False , widget=forms.DateInput(attrs={"class" : "resume-input" , "type" : "date"}) , label="Job End Date ")

        skills = forms.CharField(required=True , max_length=400 , min_length=20 , widget=forms.Textarea(attrs={"class" : "resume-input"}) , label="Your Skills ")

        class Meta:
            model = Resume
            fields = ["profile_picture" , "full_name" , "birthday" , "email" , "phone" , "school" , "degree" , "job_title" , "company" , "job_start_date" , "job_end_date" , "skills"]