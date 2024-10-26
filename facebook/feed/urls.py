from django.urls import path
from feed import views
urlpatterns=[
    path('',views.loginview,name="loginpage"),
    path('home',views.homeview,name="homepage"),
    path('about',views.aboutview,name="aboutpage"),
    path('contact',views.contactview,name="contactpage"),
    path('posts',views.postsview,name="postspage"),
    path('User',views.Userview,name="Userpage"),
]