from django.urls import path
from app1 import views

urlpatterns=[
    path('wish',views.func1,name='wishform'),
    path('name',views.func,name='rname'),
    path('prime',views.check_prime,name='pname'),
    path('armstrong',views.armstrong_checker,name='armstrongchecker'),
    path('greatestnumber',views.greatest_of_two,name='greatestoftwo'),
    path('result',views.func6,name='examresult')
]