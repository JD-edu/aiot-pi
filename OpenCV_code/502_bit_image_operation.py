import cv2


img1 = cv2.imread("flower1.jpg",cv2.IMREAD_COLOR)
img2 = cv2.imread("flower2.jpg",cv2.IMREAD_COLOR)
img_NOT = cv2.bitwise_not(img1)
img_AND = cv2.bitwise_and(img1, img2)
img_OR = cv2.bitwise_or(img1, img2)
cv2.imshow('bit_NOT',img_NOT)
cv2.imshow('bit_AND',img_AND)
cv2.imshow('bit_OR',img_OR)
cv2.waitKey(0)
cv2.destroyAllWindows()
