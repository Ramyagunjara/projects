from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def loginview(request):
    if request.method=="POST":
        Usern=request.POST.get('dog')
        passw=request.POST.get('cat')
        check=authenticate(request,username=usern,password=passw)
        if check is not None:
            login(request,check)
            if check.is_staff():
                print(check)
                return render(request,'login.html',{'res':result})
    return render(request,'login.html',)
def homeview(request):
    return render(request,'home.html')
def aboutview(request):
    return render(request,'about.html')
def contactview(request):
    return render(request,'contact.html')  
def postsview(request):
    return render(request,'posts.html')
def Userview(request):
    result=User.objects.all()
    return render(request,'User.html',{'res':result})                    