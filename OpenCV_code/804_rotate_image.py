import cv2
import numpy as np


cap = cv2.VideoCapture(0)
while (cap.isOpened()):
  ret,img = cap.read()
  cv2.imshow('my win',img)
  rows, cols = img.shape[:2]
  M = cv2.getRotationMatrix2D((cols/2, rows/2),45, 1)
  img_ROTATE = cv2.warpAffine(img, M,(cols, rows))
  cv2.imshow('move',img_ROTATE)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
cap.release()
cv2.destroyAllWindows()
