from django.shortcuts import render
from insta.models import post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser,User
# Create your views here.
def home(request):
    objs=post.objects.all()
    if request.method=="POST":
        a=request.POST.get('search')
        result=post.objects.filter(caption__icontains=a)
        return render(request,'index.html',{'posts':result})
    return render(request,'index.html',{'posts':objs})

@login_required(login_url="/admin")    
def create(request):
    if request.method=="POST":
        f=request.FILES.get('img')
        c=request.POST.get('cap')
        u=request.user
        obj=post(user=u,image=f,caption=c)
        obj.save()
    return render(request,'create.html')    