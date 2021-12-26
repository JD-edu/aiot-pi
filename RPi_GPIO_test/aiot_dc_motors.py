import RPi.GPIO as IO 
import time 

class AiotDcMotors():
	def __init__(self):
		# pin assign 
		self.pwmPin1 = 19
		self.dirPin1 = 13
		self.pwmPin2 = 12
		self.dirPin2 = 16
		# RPi GPIO setting 
		IO.setwarnings(False)
		IO.setmode(IO.BCM)
		IO.setup(self.pwmPin1, IO.OUT)
		IO.setup(self.dirPin1, IO.OUT)
		IO.setup(self.pwmPin2, IO.OUT)
		IO.setup(self.dirPin2, IO.OUT)
		# L9110 control direction pin set low 
		IO.output(self.dirPin1, False)
		IO.output(self.dirPin2, False)
		# PWM object for M1
		self.m1_pwm = IO.PWM(self.pwmPin1, 100)
		self.m1_pwm.start(0)
		# PWM object for M2
		self.m2_pwm = IO.PWM(self.pwmPin2, 100)
		self.m2_pwm.start(0)
		
	def move_forward(self, motor, speed):
		if speed > 100:
			speed = 100
		if motor == 1:
			self.m1_pwm.ChangeDutyCycle(int(speed))
		elif motor == 2:
			self.m2_pwm.ChangeDutyCycle(int(speed))
		else:
			print("motor number -> M1: 1 M2: 2")
		
	def stop(self, motor):
		if motor == 1:
			self.m1_pwm.ChangeDutyCycle(0)
		elif motor == 2:
			self.m2_pwm.ChangeDutyCycle(0)
		else:
			print("motor number -> M1: 1 M2: 2")  
			
	def release(self):
		IO.output(self.dirPin1, False) 	# releasing pins 
		IO.output(self.pwmPin1, False)
		IO.output(self.dirPin2, False) 
		IO.output(self.pwmPin2, False)
		IO.cleanup() 

if __name__ == '__main__':
	aiot_motors = AiotDcMotors()
	for a in range(3):
		aiot_motors.move_forward(1, 50)
		time.sleep(2)
		aiot_motors.stop(1)
		time.sleep(2)
	aiot_motors.release()
