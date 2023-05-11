import cv2
import numpy as np


hue = 0
color = np.uint8([[[85, 109, 215]]])
hsv_color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
hue = hsv_color[0][0][0]
print("Lower bound is :")
print("[" + str(hue-10) + ", 100, 100]\n")
print("Upper bound is :")
print("[" + str(hue+10) + ", 255, 255]\n")
print(hue)
