from django.contrib import admin

from .models import Resume

# Register your models here.
class AdminResume(admin.ModelAdmin):
    search_fields = ["created_at" , "email" , "phone" , "full_name" , "company"]

admin.site.register(Resume , AdminResume)