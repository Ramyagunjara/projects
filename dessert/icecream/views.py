from django.shortcuts import render
from icecream.models import Menu,note,contact
# Create your views here.
def func(request,no,cost):
    obj=Menu.objects.get(id=no)
    obj.price=cost
    obj.save()
    return render(request,'index.html',{'result':obj})
def func2(request):
    result=note.objects.all()
    if request.method=='POST':
        title=request.POST.get('title')
        description=request.POST.get('description')
        obj=note(title=title,description=description)
        obj.save()
        result=note.objects.all()
        return render(request,'index.html',{'res':result})
    return render(request,'index.html',{'res':result})    
def func3(request):
    result=contact.objects.all()
    if request.method=='POST':
        name=request.POST.get('name')
        number=request.POST.get('number')
        obj=contact(name=name,number=number)
        obj.save()
        result=contact.objects.all()
        return render(request,'index.html',{'res':result})
    return render(request,'index.html',{'res':result})         