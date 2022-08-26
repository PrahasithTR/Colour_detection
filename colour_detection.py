
#from tkinter import Frame
from turtle import width
import cv2
cap= cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)




while True:
    _, frame= cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width,_ = frame.shape

#height, width, depth from representing frame

#creating Centre for the frame    
    cx= int(width/2)
    cy= int(height/2)

#assining pixel value and colour logic

    pixel_centre= hsv_frame [cy, cx]
    hue_value= pixel_centre[0]
    saturation_unit= pixel_centre[1]
    value_unit= pixel_centre[2]
    
    color="Undefined"
    if value_unit>0:
        if saturation_unit>0:
            if hue_value< 5:
                color= "Red"
            elif hue_value< 22:
                color= "Orange"
            elif hue_value< 33:
                color= "Yellow"
            elif hue_value< 78:
                color = "Green"
            elif hue_value< 122:
                color= "Blue"
            elif hue_value< 170:
                color =" Violet"
            else:
                color ="Red"
        else:
            color="White"
    else:
        color="Black"
    
    pixel_centre_display= frame[cy,cx]
    b=int(pixel_centre_display[0])
    g=int(pixel_centre_display[1])
    r=int(pixel_centre_display[2])
    
    cv2.putText(frame, color,(10,50),0,1,(25,25,25),2)
    # Syntax = (frame , Text,(position in the frame x,y),font style, text size, text color,thickness)

    cv2.circle(frame,(cx,cy),5,(25,25,25),3)
    #detection point
    
    cv2.imshow("Frame",frame)
    key=cv2.waitKey(1)

# waitKey =0 (Captures the present frame)
# waitKey= 1 (Keeps the Live flow on)
    
    if key == 27: 
        break
#27 = escape key on keyboard
#used to break the live stream
# to Break the live flow if required

cap.release()
cap.destroyallwindows()


