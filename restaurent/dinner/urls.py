from django.urls import path
from dinner import views
urlpatterns=[
    path('info',views.home,name="home"),
    path('additem',views.insert_data,name="item")
]