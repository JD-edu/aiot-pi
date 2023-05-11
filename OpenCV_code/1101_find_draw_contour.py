import cv2
import numpy as np


cap = cv2.VideoCapture(0)
while (cap.isOpened()):
  ret,img = cap.read()
  img_cvt =  cv2.cvtColor( img, cv2.COLOR_BGR2GRAY)
  ret, img_thresh = cv2.threshold(img_cvt, 127, 255, cv2.THRESH_BINARY)
  cont_list, hierachy = cv2.findContours(img_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
  img_thresh = cv2.drawContours(img, cont_list, -1, (0,0,255), 1)
  cv2.imshow('my win',img)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
cap.release()
cv2.destroyAllWindows()
