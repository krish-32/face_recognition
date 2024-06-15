

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate,logout
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Q
from Dean import face_rec
from .form import *


def Attendance_view(request):
    Attendance_name=Attendance.objects.all()
    catagory = 0
    user_data=[]
    if request.user.is_authenticated:
        email=User.objects.get(username=request.user).email
        if admin_details.objects.filter(email=email):
            catagory=1
            user_data=admin_details.objects.filter(email=email)
        elif hod_register.objects.filter(email=email):
            catagory=2
            user_data=hod.objects.filter(email=email)
        elif staff_register.objects.filter(email=email):
            catagory=0
            user_data=staff_data.objects.filter(email=email)
        else:
            messages.success(request,"Login as student...")
        return render(request, 'admin/index.html',
            context={'data': Attendance_name,'catagory': catagory,'user_data':user_data})
    return render(request, 'admin/index.html',
            context={'data': Attendance_name,})


def Monitaring_image(request):
    result=0
    users=Attendance.objects.all()
    if request.method=='POST':

        search=request.POST.get('search')
        if Attendance.objects.filter(name=search):
            users=Attendance.objects.filter(name=search)
        else:
           result=1
    else:
        catagory=0
        try:
            names,times = face_rec.main()
            for name,time in zip(names,times):
                if name=='UNKNOWN':
                    pass
                else:
                    dept=data.objects.get(name=name).dept
                if Attendance.objects.filter(name=name) or name == "UNKNOWN":
                    pass
                else:
                    Attendance.objects.create(name=name,dept=dept,updated_date=time,status='Presented')
            messages.success(request,"Scanned Successfully...")                
            return redirect('Attendance_portal')
        except Exception as e:
            print(e)
    return render(request,'admin/index.html',context={'data':users,'result':result})



def staff(request):
    dean=admin_details.objects.all()
    staffs_data=hod.objects.all()
    return render(request,'admin/staff.html',context={'staffs':staffs_data,'dean':dean})



def details(request,name):
    try:
        user=staff_data.objects.filter(Select_id=name)
        if user:
            return render(request,'admin/dept_staff.html',context={'staffs':user})
        else:
            return redirect('staff_profile')
    except:
        return redirect('staff_profile')

def login_page(request):
    if request.user.is_authenticated:
        messages.success(request,"You are already had signed-in")
        return redirect('/')
    else:
        if request.method == 'POST':
            try:
                email_id = request.POST.get('email')
                password = request.POST.get('pass')
                username=User.objects.get(email=email_id.lower()).username
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('Attendance_portal')
                else:
                    messages.success(request,"Please enter a valid Passsword")
                    return redirect('login')
            except Exception as e:
                messages.success(request,"*Wrong Input",e)
    return render(request, 'login/login.html')

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')


def staff_add(request):
    form=add_staff()
    if request.method=='POST':
        form=add_staff(request.POST,request.FILES) 
        if form.is_valid():           
            form.save()
            data.objects.create(name=request.POST['name'],dept=request.POST['department'],email=request.POST['email'],photo=request.FILES['photo'])
            return redirect('Attendance_portal')
    return render(request,'admin/add_staff.html',context={'form':form})

def hod_add(request):
    hod=add_hod()
    if request.method=='POST':
        hod=add_hod(request.POST,request.FILES)
        if hod.is_valid():           
            hod.save()
            data.objects.create(name=request.POST['name'],dept=request.POST['department'],email=request.POST['email'],photo=request.FILES['photo'])
            return redirect('Attendance_portal')
    return render(request,'admin/add_staff.html',context={'form':hod})

def sign_up(request):
    user_data=user()
    if request.method=='POST':
        user_data=user(request.POST)
        user_data1=hod.objects.filter(email=request.POST['email'])
        user_data2=staff_data.objects.filter(email=request.POST['email'])
        if user_data.is_valid():
            if user_data1:         
                user_data.save()
                hod_register.objects.create(username=request.POST['username'],email=request.POST['email'],password=request.POST['password1'],confirm_pass=request.POST['password2'])
                return redirect('login')
            elif user_data2:         
                user_data.save()
                staff_register.objects.create(username=request.POST['username'],email=request.POST['email'],password=request.POST['password1'],confirm_pass=request.POST['password2'])
                return redirect('login')
            else:
                user_data.save()
                student_register.objects.create(username=request.POST['username'],email=request.POST['email'],password=request.POST['password1'],confirm_pass=request.POST['password2'])
                return redirect('login')
    return render(request,'login/sign_up.html',context={'form':user_data})