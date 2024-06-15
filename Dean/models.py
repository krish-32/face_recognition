from django.db import models
from django.contrib.auth.models import User
from pathlib import Path
def path():
    BASE_DIR = Path(__file__).resolve().parent.parent
    MEDIA_ROOT = BASE_DIR / 'static/images'
    return MEDIA_ROOT
class admin_details(models.Model):
    name =models.CharField(max_length=100, null=False, blank=False)
    position=models.CharField(max_length=100, null=True, blank=False)
    staff_id = models.BigIntegerField(blank=False)
    email = models.EmailField(unique=True, blank=True)
    phone = models.BigIntegerField(blank=False)
    department = models.CharField(blank=False, max_length=100)
    degree = models.CharField(blank=False, max_length=100)
    linkedin=models.CharField(blank=True,max_length=100)
    github=models.CharField(blank=True,max_length=100)
    whatsapp=models.CharField(blank=True,max_length=100)
    username = models.CharField(max_length=100, null=False, blank=True)
    password=models.CharField(max_length=100, null=False, blank=True)
    confirm_pass=models.CharField(max_length=100, null=False, blank=True)
    photo = models.ImageField(blank=False,upload_to=path())
    def __str__(self):
        return self.name
class data(models.Model):
    name = models.CharField(max_length=100, null=False, blank=True)
    email=models.EmailField(unique=True, blank=True)
    dept=models.CharField(blank=True,max_length=100)
    photo = models.ImageField(blank=False,upload_to=path())
    
class Attendance(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=100, null=False, blank=False)
    dept=models.CharField(blank=True,max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.CharField(blank=True,max_length=100)
    status = models.CharField(max_length=100, null=False, blank=False)
    def __str__(self):
        return self.name

class student(models.Model):
    name = models.CharField(max_length=100, null=False, blank=True)
    roll_no = models.BigIntegerField(default=True, blank=False)
    username = models.CharField(max_length=100, null=False, blank=True)
    password = models.CharField(max_length=100, null=False, blank=True)
    phone = models.BigIntegerField(default=True, blank=False)
    department = models.CharField(default=True, max_length=100)
    photo = models.ImageField(default=True, blank=False,upload_to=path())
    parent_no = models.BigIntegerField(default=True, blank=False)
    def __str__(self):
        return self.name



class hod(models.Model):
    name =models.CharField(max_length=100, null=False, blank=False)
    position=models.CharField(max_length=100, null=True, blank=True)
    staff_id = models.BigIntegerField(blank=False)
    email = models.EmailField(unique=True, blank=True)
    phone = models.BigIntegerField(blank=False)
    department = models.CharField(blank=False, max_length=100)
    degree = models.CharField(blank=False, max_length=100)
    linkedin=models.CharField(blank=True,max_length=100)
    github=models.CharField(blank=True,max_length=100)
    whatsapp=models.CharField(blank=True,max_length=100)
    photo = models.ImageField(blank=False,upload_to=path())
    def __str__(self):
        return self.department


class staff_data(models.Model):
    Select= models.ForeignKey(hod,on_delete=models.CASCADE,default=True)
    name =models.CharField(max_length=100, null=False, blank=False)
    position=models.CharField(max_length=100, null=True, blank=False)
    staff_id = models.BigIntegerField(blank=False)
    email = models.EmailField(unique=True, blank=True)
    phone = models.BigIntegerField(blank=False)
    department = models.CharField(blank=False, max_length=100)
    degree = models.CharField(blank=False, max_length=100)
    linkedin=models.CharField(blank=True,max_length=100)
    github=models.CharField(blank=True,max_length=100)
    whatsapp=models.CharField(blank=True,max_length=100)
    photo = models.ImageField(blank=False,upload_to=path())
    def __str__(self):
        return self.name



class hod_register(models.Model):
    email=models.EmailField(unique=False, blank=True)
    username = models.CharField(max_length=100, null=False, blank=True)
    password=models.CharField(max_length=100, null=False, blank=True)
    confirm_pass=models.CharField(max_length=100, null=False, blank=True)
    def __str__(self):
        return self.email

class staff_register(models.Model):
    email=models.EmailField(unique=True, blank=True)
    username = models.CharField(max_length=100, null=False, blank=True)
    password=models.CharField(max_length=100, null=False, blank=True)
    confirm_pass=models.CharField(max_length=100, null=False, blank=True)
    def __str__(self):
        return self.email
class student_register(models.Model):
    email=models.EmailField(unique=False, blank=True)
    username = models.CharField(max_length=100, null=False, blank=True)
    password=models.CharField(max_length=100, null=False, blank=True)
    confirm_pass=models.CharField(max_length=100, null=False, blank=True)
    def __str__(self):
        return self.email




