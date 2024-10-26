from django.urls import path
from insta import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('',views.home,name="homepage"),
    path('create',views.create,name="create")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)