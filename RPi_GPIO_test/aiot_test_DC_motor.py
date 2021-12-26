import RPi.GPIO as IO 
import time 

# M1 motor output 1
pwmPin1 = 19
dirPin1 = 13

# M2 motor output 2 
pwmPin2 = 12
dirPin2 = 16

# RPi GPIO setting  
IO.setwarnings(False)
IO.setmode(IO.BCM)				# define pin numbering 
IO.setup(pwmPin1, IO.OUT)		# set pin as output 
IO.setup(dirPin1, IO.OUT)
IO.setup(pwmPin2, IO.OUT)
IO.setup(dirPin2, IO.OUT)

# L9110 control direction pin set low 
IO.output(dirPin1, False)
IO.output(dirPin2, False)

# PWM object for M1
p1 = IO.PWM(pwmPin1, 100)
p1.start(0)						# PWM start. PWM duration 0 -> stop

# PWM object for M2
p2 = IO.PWM(pwmPin2, 100)
p2.start(0)

try:
	count = 1
	for a in range(3):			# testing 3 times 
		print("DC motor test: ",count)
		p1.ChangeDutyCycle(20)	# change PWM duration 20 -> speed 20%
		p2.ChangeDutyCycle(20)  
		time.sleep(2)
		p1.ChangeDutyCycle(40)	# change PWM duration 40 -> speed 40%
		p2.ChangeDutyCycle(40)
		time.sleep(2)
		p1.ChangeDutyCycle(60)  # change PWM duration 60 -> speed 60%
		p2.ChangeDutyCycle(60)
		time.sleep(2)
		p1.ChangeDutyCycle(80)	# change PWM duration 80 -> speed 80%
		p2.ChangeDutyCycle(80)
		time.sleep(2)
		p1.ChangeDutyCycle(100)	# change PWM duration 100 -> speed 100%
		p2.ChangeDutyCycle(100)
		time.sleep(2)
		count += 1

except KeyboardInterrupt:
	IO.output(dirPin1, False) 	# releasing pins 
	IO.output(pwmPin1, False)
	IO.output(dirPin2, False) 
	IO.output(pwmPin2, False)
	IO.cleanup() 






