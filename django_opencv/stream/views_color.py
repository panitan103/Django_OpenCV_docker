from django.shortcuts import render
from django.http import StreamingHttpResponse
from .Open_Camera import Camera,gen_image
from django.views.generic import View


frame = Camera()

stream_color=gen_image(frame,'color')
stream_gray=gen_image(frame,'gray')

stream_hsv=gen_image(frame,'hsv')
stream_pallet_hsv=gen_image(frame,'pallet_hsv')
stream_process_hsv=gen_image(frame,'process_hsv')

stream_rgb=gen_image(frame,'rgb')
stream_pallet_rgb=gen_image(frame,'pallet_rgb')
stream_process_rgb=gen_image(frame,'process_rgb')

stream_morph_original=gen_image(frame,'morph_original')
stream_morph_contour=gen_image(frame,'morph_contour')
stream_morph_process=gen_image(frame,'morph_process')

stream_line=gen_image(frame,'line')
stream_line_process=gen_image(frame,'line_process')

stream_circle=gen_image(frame,'circle')



def cam_stream_color(request):

    global stream_color
    
    return StreamingHttpResponse(stream_color, content_type="multipart/x-mixed-replace;boundary=frame")

def cam_stream_gray(request):

    global stream_gray

    return StreamingHttpResponse(stream_gray, content_type="multipart/x-mixed-replace;boundary=frame")

def cam_stream_hsv(request):

    global stream_hsv

    return StreamingHttpResponse(stream_hsv, content_type="multipart/x-mixed-replace;boundary=frame")
def cam_stream_pallet_hsv(request):

    global stream_pallet_hsv

    return StreamingHttpResponse(stream_pallet_hsv, content_type="multipart/x-mixed-replace;boundary=frame")
def cam_stream_process_hsv(request):

    global stream_process_hsv

    return StreamingHttpResponse(stream_process_hsv, content_type="multipart/x-mixed-replace;boundary=frame")


def cam_stream_rgb(request):

    global stream_rgb

    return StreamingHttpResponse(stream_rgb, content_type="multipart/x-mixed-replace;boundary=frame")
    
def cam_stream_pallet_rgb(request):

    global stream_pallet_rgb

    return StreamingHttpResponse(stream_pallet_rgb, content_type="multipart/x-mixed-replace;boundary=frame")
def cam_stream_process_rgb(request):

    global stream_process_rgb

    return StreamingHttpResponse(stream_process_rgb, content_type="multipart/x-mixed-replace;boundary=frame")

def cam_stream_morph_contour(request):

    global stream_morph_contour

    return StreamingHttpResponse(stream_morph_contour, content_type="multipart/x-mixed-replace;boundary=frame")

def cam_stream_morph_process(request):

    global stream_morph_process

    return StreamingHttpResponse(stream_morph_process, content_type="multipart/x-mixed-replace;boundary=frame")
    
def cam_stream_line(request):

    global stream_line

    return StreamingHttpResponse(stream_line, content_type="multipart/x-mixed-replace;boundary=frame")
def cam_stream_line_process(request):

    global stream_line_process

    return StreamingHttpResponse(stream_line_process, content_type="multipart/x-mixed-replace;boundary=frame")

def cam_stream_circle(request):

    global stream_circle

    return StreamingHttpResponse(stream_circle, content_type="multipart/x-mixed-replace;boundary=frame")