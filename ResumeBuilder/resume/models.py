from django.db import models
from django.contrib.auth.models import User

from django.core.validators import MinLengthValidator
import uuid

# Create your models here.
class Resume(models.Model):
    id = models.IntegerField(primary_key=True)
    access_id = models.SlugField(null=False , blank=False , default=uuid.uuid4 , unique=True)
    created_at = models.DateField(null=False , auto_now=True)
    profile_picture = models.ImageField()
    user = models.ForeignKey(User , related_name="user" , on_delete=models.CASCADE)
    full_name = models.CharField(null=False , blank=False , max_length=25 , validators=[MinLengthValidator(5)])
    birthday = models.DateField()
    email = models.EmailField(null=True , blank=True)
    phone = models.CharField(null=True , blank=True , max_length=12 , validators=[MinLengthValidator(12)])
    skills = models.TextField(null=False , blank=False , max_length=400 , validators=[MinLengthValidator(20)])

    school = models.CharField(null=True , blank=True , max_length=30 , validators=[MinLengthValidator(5)])
    degree = models.CharField(null=True , blank=True , max_length=10 , validators=[MinLengthValidator(2)])

    job_title = models.CharField(null=False , blank=False , max_length=15 , validators=[MinLengthValidator(2)])
    company = models.CharField(null=True , blank=False , max_length=15 , validators=[MinLengthValidator(2)])
    job_start_date = models.DateField(null=True)
    job_end_date = models.DateField(null=True)

    class Meta:
        db_table = "Resumes"

    def __str__(self):
        return self.user.username