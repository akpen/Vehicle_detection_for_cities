# Vehicle Detection in Car Images
# Ref: Creating your own Haar Cascade OpenCV Python Tutorial: 
# Site: https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/

import numpy as np
import cv2

# Vehicle Cascade xml file.
veh_cascade = cv2.CascadeClassifier('car-cascade-7-stages.xml')

img_ctr = 1
img_nm = "frame" + str(img_ctr) + ".jpg"
img = cv2.imread(img_nm)

while 1:
    print img_nm
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # image, reject levels level weights.
    vehicles = veh_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    
    for (i,(x,y,w,h)) in enumerate(vehicles):
        cv2.rectangle(img, (x,y), (x + w,y + h), (0, 0, 255), 2)
        
    cv2.imshow('Vehicle Detection', img)
#    cv2.waitKey(0)
    k = cv2.waitKey(30) & 0xFF
 

    if k == 27:   # Esc key to stop 
        img_ctr = img_ctr + 1
        if img_ctr == 20:
            break
        img_nm = "frame" + str(img_ctr) + ".jpg"
        img = cv2.imread(img_nm)
