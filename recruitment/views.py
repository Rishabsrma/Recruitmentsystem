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
    error = ""
    if request.method=="POST":
        u = request.POST['username']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                 error = "yes"    
        except:
            error = "yes"
    return render(request, 'admin_login.html', locals())

def my_experience(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    
    user = request.user
    experience = EmployeeExperience.objects.get(user=user)

    
    return render(request, 'myexperience.html', locals())


def edit_myexperience(request):
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
    return render(request, 'edit_myexperience.html', locals())


def my_education(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    
    user = request.user
    education = EmployeeEducation.objects.get(user=user)

    
    return render(request, 'my_education.html', locals())


def edit_myeducation(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    user = request.user
    education = EmployeeEducation.objects.get(user=user)
    if request.method == 'POST':
        masters = request.POST['masters']
        unim = request.POST['unim']
        yearofpassingmasters = request.POST['yearofpassingmasters']
        gpamasters = request.POST['gpamasters']

        bachelors = request.POST['bachelors']
        unib = request.POST['unib']
        yearofpassinguni = request.POST['yearofpassinguni']
        gpauni = request.POST['gpauni']

        college = request.POST['college']
        colg = request.POST['colg']
        yearofpassingcolg = request.POST['yearofpassingcolg']
        gpacolg = request.POST['gpacolg']

        school = request.POST['school']
        scl = request.POST['scl']
        yearofpassingscl = request.POST['yearofpassingscl']
        gpascl = request.POST['gpascl']

        education.masters = masters
        education.unim = unim
        education.yearofpassingmasters = yearofpassingmasters
        education.gpamasters = gpamasters
        
        education.bachelors = bachelors
        education.unib = unib
        education.yearofpassinguni = yearofpassinguni
        education.gpauni = gpauni

        education.college = college
        education.colg = colg
        education.yearofpassingcolg = yearofpassingcolg
        education.gpacolg = gpacolg

        education.school = school
        education.scl = scl
        education.yearofpassingscl = yearofpassingscl
        education.gpascl = gpascl



        try:
            education.save()
            error="no"
        except:
            error="yes"    
    return render(request, 'edit_myeducation.html', locals())


def change_password(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""

    user = request.user
    
    if request.method == 'POST':
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        
        try:
            if user.check_password(c):
                user.set_password(n)
                user.save()
                error="no"
            else:
                error = "not"    
        except:
            error="yes"    
    return render(request, 'change_password.html', locals())


def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request, 'admin_home.html')

def change_adminpassword(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""

    user = request.user
    
    if request.method == 'POST':
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        
        try:
            if user.check_password(c):
                user.set_password(n)
                user.save()
                error="no"
            else:
                error = "not"    
        except:
            error="yes"    
    return render(request, 'change_adminpassword.html', locals())


def all_employee(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    
    employee = EmployeeDetail.objects.all()
    return render(request, 'all_employee.html', locals())