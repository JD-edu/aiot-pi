import serial
import cv2
import os 
from tensorflow.keras.models import load_model
import numpy as np
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--port', required=True, help='Enter COM port number: e.g. COM20')

args = parser.parse_args()

cap = cv2.VideoCapture(0)
print(args.port)

seq = serial.Serial( baudrate=115200,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
        )

seq.port = args.port

class_labes = ["can", "pet", "cup"]
model = load_model("vgg.h5")

try:
    if seq.isOpen() == False:
        seq.open()
except IOError:
    print('COM port open error...')

while True:
    ret, img = cap.read()
    if ret:
        img_scaled = cv2.resize(img, (64, 64), interpolation=cv2.INTER_AREA)
        data = img_scaled
        data = data.astype("float")/255.0
        #print(data.shape)
        X= np.asarray([data])
        #print(X.shape)

        s = model(X, training=False)
        index = np.argmax(s)
        if index == 0:
            print("can")
            strr = 'can'
        elif index == 1:
            print("pet")
            strr = 'pet'
        elif index == 2:
            print("cup")
            strr = 'cup'
        if seq.isOpen() == True: 
            try:
                if seq.inWaiting():
                    try:
                        command = seq.readline()
                        cmd_dec = command.decode()
                        if cmd_dec[0] == 's':
                            if index == 1:
                                seq.write('can\r\n')
                            elif index == 2:
                                seq.write('pet\r\n')
                            elif index == 3:
                                seq.write('cup\r\n')
                    except ValueError:
                        print("Value error")
            except IOError:
                print("IO Error")
        
        print(index)
        cv2.putText(img, strr, (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 1)
        cv2.imshow('win', img)
        if cv2.waitKey(1)&0xff == ord('q'):
            break

cv2.destroyAllWindows()