from cobit_deep_lane_detect import CobitDeepLaneDetect
from cobit_opencv_lane_detect import CobitOpencvLaneDetect
import cv2


deep_detect = CobitDeepLaneDetect("./models/lane_navigation_final.h5")
cv_detector = CobitOpencvLaneDetect()
cap = cv2.VideoCapture('./data/car_video.avi')
while (cap.isOpened()):
  ret,img = cap.read()
  lanes, img_lane = cv_detector.get_lane(img)
  angle, img_angle = cv_detector.get_steering_angle(img_lane, lanes)
  angle_deep, img_angle_deep = deep_detect.get_steering_angle(img)
  cv2.imshow('img_deep',img_angle_deep)
  print(angle - angle_deep)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
cap.release()
cv2.destroyAllWindows()
