import cv2


img = cv2.imread("image_single_obj.jpg",cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, img_thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret, img_thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret, img_thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret, img_thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret, img_thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
cv2.imshow('orginal gray', img)
cv2.imshow('binary',img_thresh)
cv2.imshow('binary inv',img_thresh1)
cv2.imshow('truncation',img_thresh2)
cv2.imshow('to zero',img_thresh3)
cv2.imshow('to zero inv',img_thresh4)
cv2.waitKey(0)
cv2.destroyAllWindows()
