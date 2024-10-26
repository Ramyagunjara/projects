from django.urls import path
from icecream import views
urlpatterns=[
    path('info/<int:no>/<int:cost>',views.func,name="ice"),
    path('note/',views.func2,name="note"),
    path('contact/',views.func3,name="contact")
]