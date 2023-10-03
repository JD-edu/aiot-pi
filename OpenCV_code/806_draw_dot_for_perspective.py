import cv2
import numpy as np

def mouse_event(event, x, y, flags, param):
    global radius
    
    if event == cv2.EVENT_FLAG_LBUTTON:    
        cv2.circle(param, (x, y), radius, (255, 0, 0), 2)
        print(x, y)
        cv2.imshow("draw", img)

    elif event == cv2.EVENT_MOUSEWHEEL:
        if flags > 0:
            radius += 1
        elif radius > 1:
            radius -= 1

radius = 3
img = cv2.imread('rail.jpg')
print(img.shape)

cv2.imshow("draw", img)
cv2.setMouseCallback("draw", mouse_event, img)
cv2.waitKey()