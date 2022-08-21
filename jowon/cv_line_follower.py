#-*- coding:utf-8 -*-
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 320)
cap.set(4, 240)
cx = 0
cy = 0
while True:
    ret, img  = cap.read()
    img_cvt = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    img_mask1 = cv2.inRange(img_cvt, np.array([0, 100, 100]), np.array([20, 255, 255]))
    img_mask2 = cv2.inRange(img_cvt, np.array([160, 100, 100]), np.array([180, 255, 255]))
    img_mask = img_mask1 + img_mask2
    cont_list, hierachy = cv2.findContours(img_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    try:
        c = max(cont_list, key=cv2.contourArea)
        M = cv2.moments(c)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        img_con = cv2.drawContours(img, c, -1, (0,0,255), 1)
    except:
        pass
    
    
    image = cv2.circle(img, (cx,cy), 10, (0,255,0), -1)
    cv2.imshow('mask', img)
    key = cv2.waitKey(1)
    if key&0xff == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()
