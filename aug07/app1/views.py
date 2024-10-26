from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def homeview(request):
    return render(request,'home.html')
def loginview(request):
    if request.user.is_authenticated:
        return redirect('homepage') 
        if request.method=="POST":
           uname=request.POST.get('uname')
           passw=request.POST.get('passw')
           result=authenticate(request,username=uname,password=passw)
        if result is not None:
            print(uname,passw)
            login(request,result)
            return redirect('profilepage')
        else:
            return redirect('loginpage')
    return render(request,'login.html')     
def registerview(request):   
    if request.user.is_authenticated:
        messages.warning(request,"Man you already have an account !")
        return redirect('homepage')
        
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        passw=request.POST.get('passw')
        cpass=request.POST.get('cpass')
        mail=request.POST.get('mail')
        uname=request.POST.get('uname')
        print(fname,lname,passw,cpass,mail,uname)

        #validation username
        if User.objects.filter(username=uname).exists():
            messages.error(request,"Username already exists !")
            return redirect('loginpage')
        #validation for password
        if len(passw)<8:
            messages.error(request,"Password must be 8 chars")
            return redirect('registerpage')
        #validation for cpass
        if (cpass!=passw):
            messages.error(request,"Passwords doest match")
            return redirect('registerpage')
        
        obj=User.objects.create_user(username=uname,first_name=fname,last_name=lname,mail=mail,password=passw)
        obj.save()
        messages.success(request,"Hey your account is ready, Login now")
        return redirect('loginpage')

    return render(request,'register.html')



    return render(request,'register.html')
@login_required(login_url='loginpage')    
def profileview(request):
    if request.user.is_superuser:
        print(request.user.username)
        return redirect('/admin')
    return render(request,'profile.html')

@login_required(login_url='loginpage')    
def createview(request):
    return render(request,'create.html')
def singleview(request):
    return render(request,'single.html')
def logoutview(request):
    logout(request)
    return redirect('loginpage')                     