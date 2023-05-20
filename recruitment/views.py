from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import login, logout, authenticate
# Create your views here.

def index(request):
    return render(request, 'index.html')

def registration(request):
    error = ""
    if request.method == 'POST':
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['empcode']
        em = request.POST['email']
        pwd = request.POST['pwd']
        try:
            user = User.objects.create_user(first_name=fn, last_name=ln, username=em, password=pwd)
            EmployeeDetail.objects.create(user = user,empcode=ec)
            EmployeeExperience.objects.create(user = user)
            EmployeeEducation.objects.create(user = user)
            error="no"
        except:
            error="yes"    
    return render(request, 'registration.html', locals())

def emp_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['emailid']
        p = request.POST['password']
        user = authenticate(username=u, password=p)
        if user:
            login(request, user)
            error = "no"
        else:
            error = "yes"    
    return render(request, 'emp_login.html', locals())


def emp_home(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    return render(request, 'emp_home.html')

def Logout(request):
    logout(request)
    return redirect('index')

def profile(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    user = request.user
    employee = EmployeeDetail.objects.get(user=user)
    if request.method == 'POST':
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['empcode']
        dept = request.POST['department']
        designation = request.POST['designation']
        contact = request.POST['contact']
        jdate = request.POST['jdate']
        gender = request.POST['gender']

        employee.user.first_name = fn
        employee.user.last_name = ln
        employee.empcode = ec
        employee.empdept = dept
        employee.designation = designation
        employee.contact = contact
        employee.gender = gender

        if jdate:
            employee.joiningdate = jdate
        

        try:
            employee.save()
            employee.user.save()
            error="no"
        except:
            error="yes"    
    return render(request, 'profile.html', locals())


def admin_login(request):
    return render(request, 'admin_login.html')

def my_experience(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    
    user = request.user
    experience = EmployeeExperience.objects.get(user=user)

    
    return render(request, 'myexperience.html', locals())


def edit_experience(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    user = request.user
    experience = EmployeeExperience.objects.get(user=user)
    if request.method == 'POST':
        company1name = request.POST['company1name']
        company1position = request.POST['company1position']
        company1salary = request.POST['company1salary']
        company1duration = request.POST['company1duration']

        company2name = request.POST['company2name']
        company2position = request.POST['company2position']
        company2salary = request.POST['company2salary']
        company2duration = request.POST['company2duration']

        company3name = request.POST['company3name']
        company3position = request.POST['company3position']
        company3salary = request.POST['company3salary']
        company3duration = request.POST['company3duration']

        experience.company1name = company1name
        experience.company1position = company1position
        experience.company1salary = company1salary
        experience.company1duration = company1duration
        
        experience.company2name = company2name
        experience.company2position = company2position
        experience.company2salary = company2salary
        experience.company2duration = company2duration

        experience.company3name = company3name
        experience.company3position = company3position
        experience.company3salary = company3salary
        experience.company3duration = company3duration



        try:
            experience.save()
            error="no"
        except:
            error="yes"    
    return render(request, 'edit_experience.html', locals())