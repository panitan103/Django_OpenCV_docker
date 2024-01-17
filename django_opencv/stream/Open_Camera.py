import cv2
import threading
import numpy as np
from camera.views import value_hsv,value_rgb,value_morp,value_line,value_circle
import copy



class Camera(object):
    
    def __init__(self):
        #self.video = cv2.VideoCapture(0)
        self.image = cv2.imread('./static/image/prayut.jpg')     

    def __del__(self):
        self.video.release()

    def call_frame(self):
        #_,image = self.video.read()
        image = self.image.copy()

        return image

    def get_frame(self):
        
        image=self.call_frame()

        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, color = cv2.imencode('.jpg', image)
        _, gray = cv2.imencode('.jpg', gray_image)

        return color.tobytes(),gray.tobytes(),image,gray_image

    def get_frame_hsv(self):
        image=self.get_frame()[2]
        Hue,Sat,Va,Thresh_hsv=value_hsv()
        
        array = np.zeros_like(image)
        array=cv2.cvtColor(array, cv2.COLOR_BGR2HSV)
        array[:,:] = [Hue,Sat,Va]

        img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) # convert BGR to HSV
        minHSV = np.array([Hue - Thresh_hsv, Sat - Thresh_hsv, Va - Thresh_hsv])
        maxHSV = np.array([Hue + Thresh_hsv, Sat + Thresh_hsv, Va + Thresh_hsv])

        maskColor = cv2.inRange(img_hsv, minHSV, maxHSV)
        img_Color_Detector = cv2.bitwise_and(image,image,mask = maskColor)
        Pallet_image=cv2.cvtColor(array, cv2.COLOR_HSV2BGR)
        _, hsv = cv2.imencode('.jpg', img_Color_Detector)
        _, Pallet_hsv = cv2.imencode('.jpg', Pallet_image)
        _, maskColor = cv2.imencode('.jpg', maskColor)
        return hsv.tobytes(),Pallet_hsv.tobytes(),maskColor.tobytes()

    def get_frame_rgb(self):
        image=self.get_frame()[2]
        Red,Green,Blue,Thresh_rgb=value_rgb()
        img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) # convert BGR to HSV
        array = np.zeros_like(image)
        array=cv2.cvtColor(array, cv2.COLOR_BGR2HSV)
        array[:,:] = [Blue,Green,Red]

        BGR_Fillter = [Blue,Green,Red]
        hsv_Fillter = cv2.cvtColor( np.uint8([[BGR_Fillter]] ), cv2.COLOR_BGR2HSV)[0][0]

        
        lower = np.array([hsv_Fillter[0]-Thresh_rgb,hsv_Fillter[1]-Thresh_rgb,hsv_Fillter[2]-Thresh_rgb])
        upper = np.array([hsv_Fillter[0]+Thresh_rgb,hsv_Fillter[1]+Thresh_rgb,hsv_Fillter[2]+Thresh_rgb])
        
        mask_color = cv2.inRange(img_hsv, lower, upper)

        img_Color_Detector=cv2.bitwise_and(image, image, mask=mask_color )

        
        _, rgb = cv2.imencode('.jpg', img_Color_Detector)
        _, Pallet_rgb = cv2.imencode('.jpg', array)
        _, mask_color = cv2.imencode('.jpg', mask_color)
        return rgb.tobytes(),Pallet_rgb.tobytes(),mask_color.tobytes()

    def get_frame_morph(self):
        image=self.get_frame()[2]
        image_copy=copy.deepcopy(image)
        gray= self.get_frame()[3]

        thresh,kern,itera,type=value_morp()
        #print(thresh,kern,itera,type)
        if type==0:
            ret, Thresh = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY)
        if type==1:
            ret2, Thresh = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY_INV)

        #threshold select between nomal or inverse
        thresh_SELECT=Thresh

        #kernel setting
        kernel = np.ones((kern, kern), np.uint8)

        dilation = cv2.dilate(thresh_SELECT, kernel, iterations=itera)
        erosion = cv2.erode(thresh_SELECT, kernel, iterations=itera)

        ###select edge refined
        edge = erosion

        opening = cv2.morphologyEx(edge, cv2.MORPH_OPEN, kernel)
        closing = cv2.morphologyEx(edge,cv2.MORPH_CLOSE, kernel)

        ###select Filter
        Morphological = closing

        contours, hierarchy = cv2.findContours(Morphological, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        if len(contours)!=0:
            cv2.drawContours(image, contours, -1, (0,255,0), 1)
            areas = []  # list to hold all areas

            for contour in contours:
                ar = cv2.contourArea(contour)

                areas.append(ar)
            max_area_index = areas.index(max(areas))
            cnt = contours[max_area_index]
            cv2.drawContours(image, [cnt], -1, (0, 0, 255), 3)
            
            
            _,contour = cv2.imencode('.jpg', image)
        else:
            
            _,contour = cv2.imencode('.jpg', image_copy)
        
        
        Morph=cv2.cvtColor(Morphological, cv2.COLOR_GRAY2BGR)
        _, Morph = cv2.imencode('.jpg', Morph)
        
        return contour.tobytes(),Morph.tobytes()
    def get_frame_line(self):
        image=self.get_frame()[2]
        image_copy=copy.deepcopy(image)
        gray= self.get_frame()[3]
        
        
        Thresh_A,Thresh_B=value_line()
        
        edges_detection = cv2.Canny(gray,Thresh_A*10,Thresh_B*10)
        
        lines = cv2.HoughLines(edges_detection,1,np.pi/180,200)

        if lines is not None:
            for line in lines:
                rho,theta = line[0]
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a*rho
                y0 = b*rho
                x1 = int(x0 + 1000*(-b))
                y1 = int(y0 + 1000*(a))
                x2 = int(x0 - 1000*(-b))
                y2 = int(y0 - 1000*(a))
                cv2.line(image,(x1,y1),(x2,y2),(0,0,255),2)
        else:
            cv2.putText(edges_detection, 'No Line',(int(image.shape[1]/2)-150,int(image.shape[0]/2)),cv2.FONT_HERSHEY_SIMPLEX,2,(255, 255, 255), 3)
        
        edges_detection=cv2.cvtColor(edges_detection, cv2.COLOR_GRAY2BGR)
        _, edges = cv2.imencode('.jpg', image)
        _, edges_process = cv2.imencode('.jpg', edges_detection)
        
        return edges.tobytes(),edges_process.tobytes()
    def get_frame_circle(self):
        image=self.get_frame()[2]
        param1,param2,minRadius,maxRadius=value_circle()
        #param1,param2,minRadius,maxRadius=100,30,1,30
        #print(param1,param2,minRadius,maxRadius)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 5)
        rows = gray.shape[0]
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 8,
                                param1=param1, param2=param2,
                                minRadius=minRadius, maxRadius=maxRadius)
        if circles is not None:
            circles = np.uint16(np.around(circles))
            for i in circles[0, :]:
                center = (i[0], i[1])
                # circle center
                cv2.circle(image, center, 1, (0, 100, 100), 3)
                # circle outline
                radius = i[2]
                cv2.circle(image, center, radius, (255, 0, 255), 3)
        _, circle = cv2.imencode('.jpg', image)
        return circle.tobytes()
        

def gen_image(frame_get,type):
    while True:
        try :
            if type == 'color':
                frame = frame_get.get_frame()[0]
                
            if type == 'gray':
                frame = frame_get.get_frame()[1]
            if type == 'hsv':
                frame = frame_get.get_frame_hsv()[0]
            if type == 'pallet_hsv':
                frame = frame_get.get_frame_hsv()[1]
            if type == 'process_hsv':
                frame = frame_get.get_frame_hsv()[2]
            if type == 'rgb':
                frame = frame_get.get_frame_rgb()[0]
            if type == 'pallet_rgb':
                frame = frame_get.get_frame_rgb()[1]
            if type == 'process_rgb':
                frame = frame_get.get_frame_rgb()[2]
            
            if type == 'morph_contour':
                frame = frame_get.get_frame_morph()[0]
            if type == 'morph_process':
                frame = frame_get.get_frame_morph()[1]

            if type == 'line':
                frame = frame_get.get_frame_line()[0]
            if type == 'line_process':
                frame = frame_get.get_frame_line()[1]
                
            if type == 'circle':
                frame = frame_get.get_frame_circle()

            yield(b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
            #print('1')
        except:
            pass








