import cv2
import numpy as np


cap = cv2.VideoCapture(0)
while (cap.isOpened()):
  ret,img = cap.read()
  cv2.imshow('my win',img)
  img_cvt =  cv2.cvtColor( img, cv2.COLOR_BGR2GRAY)
  cv2.imshow('gray',img_cvt)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
cap.release()
cv2.destroyAllWindows()
