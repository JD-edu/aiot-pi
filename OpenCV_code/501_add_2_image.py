import cv2


img1 = cv2.imread("flower1.jpg",cv2.IMREAD_COLOR)
img2 = cv2.imread("flower2.jpg",cv2.IMREAD_COLOR)
img_add = cv2.add(img1, img2)
cv2.imshow('my win',img_add)
cv2.waitKey(0)
cv2.destroyAllWindows()
