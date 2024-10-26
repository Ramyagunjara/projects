from django.shortcuts import render
from dinner.models import menu
# Create your views here.
def home(request):
    result=menu.objects.all()
    if request.method=='POST':
        sno=int(request.POST.get('sno'))
        if menu.objects.filter(id=sno).exists:
            abc=menu.objects.get(id=sno)
        else:
            abc=None   
            return render(request,'index.html',{'res':result},{'res2':abc})    
    return render(request,'index.html',{'res':result})  
def insert_data(request):
    result=menu.objects.all()
    if request.method=='POST':
        dish=request.POST.get('food')
        cost=request.POST.get('food_price')
        obj=menu(Item=dish,price=cost)
        obj.save()      
        result=menu.objects.all()
        return render(request,'form.html',{'res':result})
    return render(request,'form.html',{'res':result}) 
       