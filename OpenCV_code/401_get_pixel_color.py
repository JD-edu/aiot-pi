import cv2


img = cv2.imread("lena.jpg",cv2.IMREAD_COLOR)
blue, green, red = img[100, 100]
cv2.imshow('my win',img)
print(blue)
print(green)
print(red)
cv2.waitKey(0)
cv2.destroyAllWindows()
