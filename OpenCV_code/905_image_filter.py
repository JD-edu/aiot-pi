#-*- coding:utf-8 -*-
import cv2
import numpy as np

def nothing(x):
    pass

img = cv2.imread('lena.jpg')

cv2.namedWindow('image')
cv2.createTrackbar('K','image',1,20, nothing)

while(1):
    if cv2.waitKey(1) & 0xFF == 27:
        break
    k = cv2.getTrackbarPos('K','image')

    #(0,0)이면 에러가 발생함으로 1로 치환
    if k == 0:
        k = 1

    # trackbar에 의해서 (1,1) ~ (20,20) kernel생성
    kernel = np.ones((k,k),np.float32)/(k*2)
    dst = cv2.filter2D(img,-1,kernel)

    cv2.imshow('image',dst)

cv2.destroyAllWindows()