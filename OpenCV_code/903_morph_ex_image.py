import cv2
import numpy as np


cap = cv2.VideoCapture(0)
while (cap.isOpened()):
  ret,img = cap.read()
  cv2.imshow('img',img)
  img_cvt =  cv2.cvtColor( img, cv2.COLOR_BGR2HSV)
  # Orange color
  # RGB: 215 109 85
  # Hue value: 6
  img_mask = cv2.inRange( img_cvt, (np.array([ -4, 100, 100])), (np.array([ 16, 255, 255])))
  cv2.imshow('mask',img_mask)
  kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
  img_morph = cv2.morphologyEx(img_mask, cv2.MORPH_CLOSE, kernel)
  cv2.imshow('morph',img_morph)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
cap.release()
cv2.destroyAllWindows()
