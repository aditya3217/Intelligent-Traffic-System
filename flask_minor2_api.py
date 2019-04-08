import os
import urllib
import base64
from flask import Flask,request
from flask import Flask,render_template, redirect,url_for
from werkzeug.utils import secure_filename
import glob
import cv2
import numpy as np
import predict
from PIL import Image
import io 
import base64

import serial
import time

road_images = {}
road_images['left'] = ''
road_images['right'] = ''
road_images['up'] = ''
road_images['down'] = ''

#path_to_images= r'C:\Users\india\minor2\recieved_images'
UPLOAD_FOLDER = r'D:\test'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def func():
	if(road_images['down'] != '' and road_images['up'] != '' and road_images['left'] != '' and road_images['right'] != '') :
			
		drn = predict.predict_side(road_images)
		bluetooth_integrate(drn)
		print(road_images)
		road_images['down'] = '' 
		road_images['up'] = '' 
		road_images['left'] = '' 
		road_images['right'] = ''
	return

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
    
@app.route('/bacon',methods=['GET','POST'])
def bacon():
    if request.method=='POST':
        return 'Method used is POST'
    else:
        return 'Method used is GET'


@app.route('/find' , methods = ['GET' , 'POST'])
def find():
    if request.method == 'GET':
        return "HELLO"



		

		
		
		
		
		
		
		
		
		
		
		
		


def upload_file(image , direction):


    img = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)
     
    red_lower=np.array([130,20,120],np.uint8)
    red_upper=np.array([200,255,255],np.uint8)
    
    green_lower=np.array([33,75,40],np.uint8)
    green_upper=np.array([150,255,255],np.uint8)
    
    yellow_lower=np.array([22,60,150],np.uint8)
    yellow_upper=np.array([80,255,255],np.uint8)
    
    kernelOpen=np.ones((20,20))
    kernelClose=np.ones((25,25))
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    height, width = img.shape[:2]
    max_height = 300
    max_width = 300

    if max_height < height or max_width < width:
        # get scaling factor
        scaling_factor = max_height / float(height)
        if max_width/float(width) < scaling_factor:
                scaling_factor = max_width / float(width)
        # resize image
    img_red = cv2.resize(img, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)

    img_yellow= img_red
    img_green = img_red
                #img=cv2.resize(img,(200,200))

                #convert BGR to HSV
    imgHSV_red = cv2.cvtColor(img_red,cv2.COLOR_BGR2HSV)
    imgHSV_yellow = cv2.cvtColor(img_yellow,cv2.COLOR_BGR2HSV)
    imgHSV_green = cv2.cvtColor(img_green,cv2.COLOR_BGR2HSV)
                # create the Mask
    mask_red =cv2.inRange(imgHSV_red,red_lower,red_upper)
    mask_green =cv2.inRange(imgHSV_green,green_lower,green_upper)
    mask_yellow =cv2.inRange(imgHSV_yellow,yellow_lower,yellow_upper)
                #morphology
    maskOpen_red =cv2.morphologyEx(mask_red,cv2.MORPH_OPEN,kernelOpen)
    maskClose_red =cv2.morphologyEx(maskOpen_red,cv2.MORPH_CLOSE,kernelClose)

            # cv2.imshow("maskOpen_red" , maskOpen_red)
            # cv2.imshow("maskClose_red" , maskClose_red)

    maskOpen_green =cv2.morphologyEx(mask_green,cv2.MORPH_OPEN,kernelOpen)
    maskClose_green =cv2.morphologyEx(maskOpen_green,cv2.MORPH_CLOSE,kernelClose)

            # cv2.imshow("maskOpen_green" , maskOpen_green)
            # cv2.imshow("maskClose_green" , maskClose_green)

    maskOpen_yellow =cv2.morphologyEx(mask_yellow,cv2.MORPH_OPEN,kernelOpen)
    maskClose_yellow =cv2.morphologyEx(maskOpen_yellow,cv2.MORPH_CLOSE,kernelClose)

            # cv2.imshow("maskOpen_yellow" , maskOpen_yellow)
            # cv2.imshow("maskClose_yellow" , maskClose_yellow)

    maskFinal_red = maskClose_red
    maskFinal_yellow = maskClose_yellow
    maskFinal_green = maskClose_green

    _,conts_red,h=cv2.findContours(maskFinal_red.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    _,conts_yellow,h=cv2.findContours(maskFinal_yellow.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    _,conts_green,h=cv2.findContours(maskFinal_green.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    cv2.drawContours(img_red,conts_red,-1,(255,0,0),3)

    cv2.drawContours(img_yellow,conts_yellow,-1,(255,0,0),3)

    cv2.drawContours(img_green,conts_green,-1,(255,0,0),3)

    for i in range(len(conts_red)):
        x,y,w,h=cv2.boundingRect(conts_red[i])
        cv2.rectangle(img_red,(x,y),(x+w,y+h),(0,0,255), 2)
        cv2.putText(img_red, str(i+1),(x,y+h),font,0.30 ,(0,255,255),1)


    for i in range(len(conts_yellow)):
        x,y,w,h=cv2.boundingRect(conts_yellow[i])
        cv2.rectangle(img_yellow,(x,y),(x+w,y+h),(0,0,255), 2)
        cv2.putText(img_yellow, str(i+1),(x,y+h),font,0.30 ,(0,255,255),1)


    for i in range(len(conts_green)):
        x,y,w,h=cv2.boundingRect(conts_green[i])
        cv2.rectangle(img_green,(x,y),(x+w,y+h),(0,0,255), 2)
        cv2.putText(img_green, str(i+1),(x,y+h),font,0.30 ,(0,255,255),1)


#     print("red : " , len(conts_red))
#     print("yellow : " , len(conts_yellow))
#     print("green: " , len(conts_green))
            
    red = str(len(conts_red))
    yellow = str(len(conts_yellow))
    green = str(len(conts_green))
#             k = cv2.waitKey(0)
#             if k == 27:         # wait for ESC key to exit
#                 cv2.destroyAllWindows()
    road_images[direction] = red+" "+yellow+" "+green
    
	
 
    return red+" "+yellow+" "+green

def bluetooth_integrate(drn):
    s = serial.Serial('COM6', 9600,timeout = 1)
    #print("connected!")
    time.sleep(5)
    s.write(drn.encode('utf-8'))
    print("Sent Message!")	
    return
	
@app.route('/image',methods=['GET','POST'])
def greet():
    direction = request.form['dir']
    #print(direction)
    im = Image.open(io.BytesIO(base64.b64decode(request.form['image'])))
    upload_file(im , direction)
    #print(direction , ' road image received')
    return ""


#172.16.104.126
#mob-192.168.43.253

if(__name__=="__main__"):
    app.run(debug=True,host='192.168.43.203',port=5002,use_reloader=False)





