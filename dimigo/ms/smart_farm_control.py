'''
example: python smart_farm_control --light 8  --temp 25 --soil 50 --port COM20
'''

import serial 
import time 
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--light', required=True, help='Enter light on time: e.g. 8')
parser.add_argument('--temp', required=True, help='Enter temperature threshold value(Celcius): e.g. 25')
parser.add_argument('--soil', required=True, help='Enter soil moisture threshold value(%): e.g. 50')
parser.add_argument('--port', required=True, help='Enter COM port number: e.g. COM20')

args = parser.parse_args()

print(args.light)
print(args.temp)
print(args.soil)
print(args.port)


seq = serial.Serial( baudrate=115200,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
        )

seq.port = args.port
temp_threshold = int(args.temp)
soil_threshold = int(args.soil)
light_on = int(args.light)

try:
    if seq.isOpen() == False:
        seq.open()
except IOError:
    print('COM port open error...')

while True: 
    if seq.isOpen() == True:  
        try:
            if seq.inWaiting():
                try:
                    command = seq.readline()
                    cmd_dec = command.decode()
                    cmd_sub = cmd_dec[:(len(cmd_dec)-2)]
                    if cmd_sub[0] == 'a':
                        a = cmd_sub.index('a')
                        b = cmd_sub.index('b')
                        c = cmd_sub.index('c')
                        d = cmd_sub.index('d')
                        e = cmd_sub.index('e')
                        temperature = float(cmd_sub[a+1:b])
                        humidity = float(cmd_sub[b+1:c])
                        light  = float(cmd_sub[c+1:d])
                        soil = int(cmd_sub[d+1:e])
                        print(temperature, humidity, soil, light)
                        
                        # 여기에서 일정온도 이상이면 fan을 on 하는 명령을 내보낸다. 
                        # seq.println('cc')
                        if temperature > temp_threshold:
                            seq.write('c\r\n'.encode())
                        else:
                            seq.write('f\r\n'.encode())
                        
                        # 여기에서는 soil 수분이 부족하면 경고를 프린트하는 코드를 넣는다
                        if soil > soil_threshold:
                            print("Add water")
                        else:
                            print("Enough water")

                        # 여기에서는 현재 시간을 파악해서 LED를 on할것인지 off할것인지 결정한다. 

                
                        # 여기서 이미지 쵤영하고 추론파일로 검사해서 성장상태를 파악하는 코드  


                        # 여기에서 센서 데이터 성장상태 데이터를 pysonDB에 저장하는 코드 
                except ValueError:
                    print("value error")
                    
        except IOError:
            print("IO error")
        


