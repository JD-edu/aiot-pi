import numpy as np
import cv2


img = np.zeros((320, 240, 3), np.uint8)
cv2.line(img, (10, 10), (100, 100), (0,0,255), 1 )
cv2.imshow('my win',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
