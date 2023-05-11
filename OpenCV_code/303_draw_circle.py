import numpy as np
import cv2


img = np.zeros((320, 240, 3), np.uint8)
cv2.circle(img, (100, 100), 50, (0,0,255), 2 )
cv2.circle(img, (150, 150), 150, (255,255,51), 2 )
cv2.imshow('my win',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
