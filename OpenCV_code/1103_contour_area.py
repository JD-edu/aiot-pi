#-*- coding:utf-8 -*-
import cv2
import numpy as np

img = cv2.imread('image_single_obj.jpg')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray,127,255,0)

contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
img_thresh = cv2.drawContours(img, contours, 0, (0,0,255), 2)



# 첫번째 contours의 moment 특징 추출
cnt = contours[0]
M = cv2.moments(cnt)

#print(M.items())
area = cv2.contourArea(cnt)
print(M['m00'])
print(area)

cv2.imshow('win', img)
cv2.waitKey(0)
cv2.destroyAllWindows()