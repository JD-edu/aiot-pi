#-*- coding:utf-8 -*-
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 320)
cap.set(4, 240)

while True:
    ret, image = cap.read()
    imgray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    #threshold를 이용하여 binary image로 변환
    ret, thresh = cv2.threshold(imgray,127,255,0)

    #contours는 point의 list형태. 예제에서는 사각형이 하나의 contours line을 구성하기 때문에 len(contours) = 1. 값은 사각형의 꼭지점 좌표.
    #hierachy는 contours line의 계층 구조
    contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    c = max(contours, key=cv2.contourArea)
    M = cv2.moments(c)
    image = cv2.drawContours(image, c, -1, (0,255,0), 3)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    print(cx, cy)
    image = cv2.circle(image, (cx,cy), 10, (0,0,255), -1)
    cv2.imshow('image', image)
    key = cv2.waitKey(1)
    if key&0xff == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()
