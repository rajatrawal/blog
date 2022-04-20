from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Account(models.Model):
    type = models.CharField(choices=[('D','Doctor'),('P','Patient')],max_length=7,default='P')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='myApp/images')
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=50)
    
    