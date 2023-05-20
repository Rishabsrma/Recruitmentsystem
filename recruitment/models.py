from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class EmployeeDetail(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    empcode = models.CharField(max_length=50,null=True)   
    empdept = models.CharField(max_length=100,null=True) 
    designation = models.CharField(max_length=100,null=True) 
    contact = models.CharField(max_length=15,null=True) 
    gender = models.CharField(max_length=25,null=True) 
    joiningdate = models.DateField(null=True) 

    def __str__(self):
        return self.user.username


class EmployeeEducation(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    masters = models.CharField(max_length=100, null=True)   
    unim = models.CharField(max_length=200,null=True) 
    yearofpassingmasters = models.CharField(max_length=20,null=True) 
    gpamasters = models.CharField(max_length=30,null=True)

    bachelors = models.CharField(max_length=100, null=True)   
    unib = models.CharField(max_length=200,null=True) 
    yearofpassinguni = models.CharField(max_length=20,null=True) 
    gpauni = models.CharField(max_length=30,null=True) 

    college = models.CharField(max_length=100, null=True)   
    colg = models.CharField(max_length=200,null=True) 
    yearofpassingcolg = models.CharField(max_length=20,null=True) 
    gpacolg = models.CharField(max_length=30,null=True) 

    school = models.CharField(max_length=100, null=True)   
    scl = models.CharField(max_length=200,null=True) 
    yearofpassingscl = models.CharField(max_length=20,null=True) 
    gpascl = models.CharField(max_length=30,null=True) 

    def __str__(self):
        return self.user.username
    

class EmployeeExperience(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    company1name = models.CharField(max_length=100, null=True)   
    company1position = models.CharField(max_length=100,null=True) 
    company1salary = models.CharField(max_length=100,null=True) 
    company1duration = models.CharField(max_length=100,null=True) 
    company2name = models.CharField(max_length=100, null=True)   
    company2position = models.CharField(max_length=100,null=True) 
    company2salary = models.CharField(max_length=100,null=True) 
    company2duration = models.CharField(max_length=100,null=True) 
    company3name = models.CharField(max_length=100, null=True)   
    company3position = models.CharField(max_length=100,null=True) 
    company3salary = models.CharField(max_length=100,null=True) 
    company3duration = models.CharField(max_length=100,null=True) 
   

    def __str__(self):
        return self.user.username    