import cv2


cap = cv2.VideoCapture(0)
while (cap.isOpened()):
  ret,img = cap.read()
  cv2.imshow('my win',img)
  img_RESIZE = cv2.resize(img, None, fx=0.4, fy=0.9, interpolation=cv2.INTER_AREA)
  cv2.imshow('resize',img_RESIZE)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
cap.release()
cv2.destroyAllWindows()
