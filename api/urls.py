from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from vplay import views,upload
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.index,name="index"),
    path('api/index/',views.hello,name="hello"),
    path('api/upload/',upload.upload,name="upload"),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)