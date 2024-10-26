from django.shortcuts import render

# Create your views here.
def func1(request):    
    a=request.POST.get('sname')
    #print("Hi"+a)
    return render(request,'index.html',{'res':a})  
def func(request):
    result=None
    if request.method=="POST":
        
        a=int(request.POST.get('num'))
        if a%2==0:
            result=True
        else:
            result=False
    return render(request,'evenodd.html',{'res':result}) 
def check_prime(request):
    number = request.GET.get('number')
    context = {'number': number}

    if number:
        try:
            number = int(number)
            is_prime = is_prime_number(number)
            context['is_prime'] = is_prime
        except ValueError:
            context['error_message'] = "Invalid input. Please enter a valid integer."

    return render(request,'prime.html',context)

def is_prime_number(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True      

def is_armstrong(number):
    num_str=str(number)
    num_len=len(num_str)
    total=sum(int(digit) ** num_len for digit in num_str)
    return total==number

def armstrong_checker(request):
    result=None
    number=None
    if request.method=='POST':
        number = int(request.POST.get('number'))
        result = is_armstrong(number)
    return render(request,'armstrong.html',{'result': result, 'number': number})

def greatest_of_two(request):
    result = None
    num1 = num2 = None
    if request.method == 'POST':
        num1 = int(request.POST.get('num1'))
        num2 = int(request.POST.get('num2'))
        result = max(num1, num2)
    return render(request,'twonumbers.html',{'result': result, 'num1': num1, 'num2': num2})
def func6(request):
    if request.method == 'POST':
        a = request.POST.get('sname')
        print(request.POST)
        result = None
        students = {
            'routes': [
                {'rollno': '214g1a0581', 'name': 'ramya', 'ps': 6, 'fs': 0},
                {'rollno': '214g1a05b3', 'name': 'thrisha', 'ps': 4, 'fs': 1},
                {'rollno': '214g1a0589', 'name': 'pavani', 'ps': 5, 'fs': 1}
            ]
        }
        for record in students['routes']:
            if record['rollno'] == a:
                result = record
                break
        if result is not None:
            return render(request, 'examresults.html', {'student': result})
        else:
            return render(request, 'examresults.html')
    else:
        # Handle GET request or other request methods
        return render(request, 'examresults.html')
             
   

              