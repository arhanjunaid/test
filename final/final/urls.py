"""final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views

from finalapp.views import email,email1,password_reset_change,viewindex,password_reset_done,login_view,password_reset,login_view1,register_view,logout_view,success,login_view2,upload,Image_View,download,download_csv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',viewindex),
    path('login/',login_view),
    path('login2/',login_view1),
    path('login3/',login_view2),
    path('register/',register_view),
    path('logout/',logout_view),
    path('success/',success),
    path('upload/',upload),
    path('image/',Image_View),
    path('excel/',download),
    path('csv/',download_csv),
    path('accounts/',include("django.contrib.auth.urls")),
    path('reset/',password_reset),
    path('reset_done/',password_reset_done),
    path('reset_change/',password_reset_change),
    path('check/',email),
    path('check1/',email1),





]

