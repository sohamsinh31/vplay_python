from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from vplay import views,upload
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.index,name="index"),
    path('my/',views.hello,name="hello"),
    path('upload/',upload.upload,name="upload")
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
