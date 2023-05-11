from adafruit_servokit import ServoKit
from cobit_car_motor_l9110 import CobitCarMotorL9110
from cobit_deep_lane_detect import CobitDeepLaneDetect
import cv2


servo = ServoKit(channels=16)
motor = CobotCarMotorL9110()
deep_detect = CobitDeepLaneDetect("./models/lane_navigation_final.h5")
motor.motor_all_start(12)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,240)
while (cap.isOpened()):
  ret,img = cap.read()
  angle_deep, img_angle_deep = deep_detect.get_steering_angle(img)
  servo.servo[0].angle = angle_deep
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
cap.release()
cv2.destroyAllWindows()
motor.motor_all_stop()
