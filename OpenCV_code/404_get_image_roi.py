import cv2


img = cv2.imread("lena.jpg",cv2.IMREAD_COLOR)
cv2.imshow('my win',img)
array_ROI = img[100:200, 300:400]
img[0:100,0:100] = array_ROI
cv2.imshow('my ROI',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
