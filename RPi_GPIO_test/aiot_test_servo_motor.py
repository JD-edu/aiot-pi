import time
# importing adafruit PCA9685 control module
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

count = 0
for a in range(3):
	print("Servo motor test: ", count)
	print("Set servo 120 degree")
	kit.servo[0].angle = 120
	time.sleep(1)
	print("Set servo 90 degree")
	kit.servo[0].angle = 90
	time.sleep(1)
	print("set servo 60 degree")
	kit.servo[0].angle = 60
	time.sleep(1)
	count += 1
	
kit.servo[0].angle = 90
