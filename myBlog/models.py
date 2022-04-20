
from pyexpat import model
from django.db import models
from myApp.models import Account
from datetime import timedelta,datetime
# Create your models here.
class Post(models.Model):
    id =  models.AutoField(primary_key=True)
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    image = models.ImageField(upload_to ='blog/images')
    title = models.CharField(max_length=500,default='')
    category = models.CharField(choices=(
        ('mental health','mental health'),
        ('heart disease','heart disease'),
        ('covid19','covid19'),
        ('immunization','immunization'),
    ),max_length=13)
    summary = models.TextField(max_length=500)
    content = models.TextField(max_length=500000)
    is_draft = models.CharField(choices=(
        ('true',True),
        ('false',False)
    ),max_length=5)
    time = models.DateTimeField(auto_now=True)
    
class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    doctor = models.CharField(max_length=500,default='')
    category = models.CharField(choices=(
        ('mental health','mental health'),
        ('heart disease','heart disease'),
        ('covid19','covid19'),
        ('immunization','immunization'),
    ),max_length=13)
    time = models.DateTimeField(default=datetime.now())
    end_time = models.DateTimeField(default=datetime.now()+timedelta(minutes=45))



    
    