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

from enum import Flag
from django.urls import path

from . import views_color




urlpatterns = [
    
    path('cam_stream_color/', views_color.cam_stream_color),
    path('cam_stream_gray/', views_color.cam_stream_gray),
    path('cam_stream_hsv/', views_color.cam_stream_hsv),
    path('cam_stream_pallet_hsv/', views_color.cam_stream_pallet_hsv),
    path('cam_stream_process_hsv/', views_color.cam_stream_process_hsv),

    path('cam_stream_rgb/', views_color.cam_stream_rgb),
    path('cam_stream_pallet_rgb/', views_color.cam_stream_pallet_rgb),
    path('cam_stream_process_rgb/', views_color.cam_stream_process_rgb),
   
    path('cam_stream_morph_contour/', views_color.cam_stream_morph_contour),
    path('cam_stream_morph_process/', views_color.cam_stream_morph_process),

    path('cam_stream_line/', views_color.cam_stream_line),
    path('cam_stream_line_process/', views_color.cam_stream_line_process),

    path('cam_stream_circle/', views_color.cam_stream_circle),
    
    

]

