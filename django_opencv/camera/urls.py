"""GUI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from aiohttp import request
from django.contrib import admin
from django.urls import path

from . import views
#from django.conf.urls import url


urlpatterns = [
    path('',views.index.as_view()),
    path('setting/', views.setting),
    #path('cam_stream_color', views.cam_stream_color,name='cam_stream_color'),
    #path('cam_stream_gray', views.cam_stream_gray,name='cam_stream_gray'),
    
    path('image/image/', views.cam),


    path('color/rgb/', views.rgb),

    path('color/hsv/', views.hsv),

    
    path('object/line/', views.line),

    path('object/circle/', views.circle),

    path('object/morp/', views.morp),



]

