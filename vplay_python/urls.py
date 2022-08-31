from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vplay.urls')),
    path('', include('api.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
