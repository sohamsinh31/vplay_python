from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from vplay import views,upload
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.index,name="index"),
    path('my/',views.hello,name="hello"),
    path('upload/',upload.upload,name="upload"),
    path('login/',views.login_user,name="login"),
    path('signup/',views.signup,name="signup"),
    path('video/<int:id>',views.video,name="signup"),
    path('accounts/login/',views.login_user,name="login2"),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
