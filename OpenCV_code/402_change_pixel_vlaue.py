import cv2


img = cv2.imread("lena.jpg",cv2.IMREAD_COLOR)
img[10, 10] = [255, 255, 255]
img[10, 11] = [255, 255, 255]
img[11, 10] = [255, 255, 255]
img[11, 11] = [255, 255, 255]
cv2.imshow('my win',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
