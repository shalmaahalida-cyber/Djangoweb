from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('/sosmed/')),
    path('sosmed/', include('sosmed.urls')),
    path('admin/', admin.site.urls),
]