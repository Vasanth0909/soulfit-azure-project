"""
URL configuration for soulfitpro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
import sqlite3

from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import include, path
from fitapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("fitapp.urls")),
    path('',views.home ,name="home"),
    path('',views.register_view ,name="register"),
    path('',views.ridepopup ,name="ridepopup"),
    path('',views.soul ,name="soul"),
    path('',views.spirit ,name="spirit"),
    path('',views.soulreg,name="soulreg"),
    path('',views.gear ,name="gear"),
    path('',views.fitzz ,name="fitzz"),
    path('',views.cheackout ,name="cheackout"),
    path('',views.login ,name="login"),
    path('',views.bot ,name="bot"),
    path('',views.signup, name="signup"),
    path('',views.register,name="register")
]
