from cobit_opencv_lane_detect import CobitOpencvLaneDetect
from cobit_car_motor_l9110 import CobitCarMotorL9110
from adafruit_servokit import ServoKit
import cv2


cv_detector = CobitOpencvLaneDetect()
motor = CobotCarMotorL9110()
servo = ServoKit(channels=16)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,240)
motor.motor_all_start(15)
while (cap.isOpened()):
  ret,img = cap.read()
  lanes, img_lane = cv_detector.get_lane(img)
  angle, img_angle = cv_detector.get_steering_angle(img_lane, lanes)
  cv2.imshow('img_angle',img_angle)
  servo.servo[0].angle = angle
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
cap.release()
cv2.destroyAllWindows()
motor.motor_all_stop()
