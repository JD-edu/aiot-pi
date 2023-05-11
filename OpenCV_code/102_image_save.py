import cv2


img = cv2.imread("lena.jpg",cv2.IMREAD_COLOR)
cv2.imshow('my win',img)
key = cv2.waitKey(0)&0xff
if key != 27:
  cv2.imwrite('lena_2.jpg',img)
cv2.destroyAllWindows()
