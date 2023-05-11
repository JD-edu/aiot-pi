import cv2


img = cv2.imread("morph_char.png",cv2.IMREAD_COLOR)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
img_dilate = cv2.dilate(img, kernel, iterations = 1)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
img_erode = cv2.erode(img, kernel, iterations = 1)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
img_morph = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
img_morph1 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
img_morph2 = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
img_morph3 = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
img_morph4 = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow('org',img)
cv2.imshow('dilation',img_dilate)
cv2.imshow('erode',img_erode)
cv2.imshow('open',img_morph)
cv2.imshow('closed',img_morph1)
cv2.imshow('grad',img_morph2)
cv2.imshow('top hat',img_morph3)
cv2.imshow('black hat',img_morph4)
cv2.waitKey(0)
cv2.destroyAllWindows()
