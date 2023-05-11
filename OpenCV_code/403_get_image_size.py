import cv2


img = cv2.imread("lena.jpg",cv2.IMREAD_COLOR)
img_size = img.size
rows, columns, channels = img.shape
print(img_size)
print(columns)
print(rows)
print(channels)
cv2.imshow('my win',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
