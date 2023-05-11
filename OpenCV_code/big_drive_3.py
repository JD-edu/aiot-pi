from cobit_opencv_lane_detect import CobitOpencvLaneDetect
import cv2


index = 0


cv_detector = CobitOpencvLaneDetect()
cap = cv2.VideoCapture('./data/car_video.avi')
while (cap.isOpened()):
  ret,img = cap.read()
  lanes, img_lane = cv_detector.get_lane(img)
  angle, img_angle = cv_detector.get_steering_angle(img_lane, lanes)
  cv2.imwrite("%s_%03d_%03d.png" % ("./data/lane_image", index, angle), img)
  index += 1
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
cap.release()
cv2.destroyAllWindows()
