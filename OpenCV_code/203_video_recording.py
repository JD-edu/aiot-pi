import cv2


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,240)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
writer = cv2.VideoWriter('video.avi', fourcc, 25.0, (320, 240))
while (cap.isOpened()):
  ret,img = cap.read()
  cv2.imshow('my win',img)
  writer.write(img)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
cap.release()
cv2.destroyAllWindows()
