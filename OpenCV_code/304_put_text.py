import numpy as np
import cv2


img = np.zeros((320, 240, 3), np.uint8)
cv2.putText(img , 'This is test!', (100, 100) , cv2.FONT_HERSHEY_SIMPLEX, 1, (102,255,255))
cv2.putText(img , 'Hello world!', (50, 100) , cv2.FONT_HERSHEY_SIMPLEX, 2, (255,204,51))
cv2.imshow('my win',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
