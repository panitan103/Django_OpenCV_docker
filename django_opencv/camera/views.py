from django.shortcuts import render
from django.http import HttpResponse,StreamingHttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.views.generic import View



# Create your views here.
class index(View):
    def get(self,request):
        text=request.GET.get('button_text')
        #print(text)
        return render(request,"index.html")

def setting(request):
    return render(request,"setting.html")

def cam(request):
    return render(request,"cam.html")

def rgb(request):
    global Red,Green,Blue,Thresh_rgb
    Red=request.GET.get('R_Value')
    Green=request.GET.get('G_Value')
    Blue=request.GET.get('B_Value')
    Thresh_rgb=request.GET.get('Thresh_value')
    
    return render(request,"color_rgb.html")
def value_rgb():
    global Red,Green,Blue,Thresh_rgb
    
    return int(Red),int(Green),int(Blue),int(Thresh_rgb)

'''
def hsv(request):
    
    return render(request,"color_hsv.html")
'''

def hsv(request):
    global Hue,Sat,Va,Thresh_hsv,Update
    Hue=request.GET.get('H_Value')
    Sat=request.GET.get('S_Value')
    Va=request.GET.get('V_Value')
    Thresh_hsv=request.GET.get('Thresh_value')
    Update=request.GET.get('Update')
    
    return render(request,"color_hsv.html")
def value_hsv():
    global Hue,Sat,Va,Thresh_hsv,Update
    
    return int(Hue),int(Sat),int(Va),int(Thresh_hsv)


def line(request):
    global thresh_A_Value,thresh_B_Value
    thresh_A_Value=request.GET.get('thresh_A_Value')
    thresh_B_Value=request.GET.get('thresh_B_Value')

    return render(request,"line.html")
def value_line():
    global thresh_A_Value,thresh_B_Value
    
    return int(thresh_A_Value),int(thresh_B_Value)


def circle(request):
    global param1,param2,maxRadius,minRadius_out
    param1=request.GET.get('param1_out')
    param2=request.GET.get('param2_out')
    minRadius_out=request.GET.get('minRadius_out')
    maxRadius=request.GET.get('maxRadius_out')
    
    
    return render(request,"circle.html")
def value_circle():
    global param1,param2,maxRadius,minRadius_out
    
    return int(param1),int(param2),int(minRadius_out),int(maxRadius)


def morp(request):
    global thresh_morp,kern,iter,thresh_type
    thresh_morp=request.GET.get('thresh_morp_Value')
    kern=request.GET.get('kern_Value')
    iter=request.GET.get('iter_Value')
    thresh_type=request.GET.get('thresh_morp_type')
    return render(request,"morp.html")

def value_morp():
    global thresh_morp,kern,iter,thresh_type
    
    return int(thresh_morp),int(kern),int(iter),int(thresh_type)