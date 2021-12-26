'''
Project description
- Checking temperature 
- If temperature is too high, turn on fan 
'''

import serial
import time 

temperature = 0
humidity = 0
distance = 0
light = 0

seq = serial.Serial(
        baudrate=115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )


seq.port = "/dev/ttyACM0"
seq.open()

while True:
    if seq.isOpen() == True:
        if seq.inWaiting():         
            packets = seq.readline()
            a = packets.index('a')
            b = packets.index('b')
            c = packets.index('c')
            d = packets.index('d')
            e = packets.index('e')
            temperature  = float(packets[a+1:b])
            humidity  = float(packets[b+1:c])
            distance  = float(packets[c+1:d])
            light = float(packets[d+1:e])
            print(temperature, humidity, distance, light)
            
            # put yor code here 
