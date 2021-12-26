#-*- coding:utf-8 -*-
import serial 
import time

class AiotSerialManager:
   
    def __init__(self, serial_port):

        self.seq = serial.Serial(
            baudrate=115200,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
        )
        self.seq.port = serial_port
       
    def running(self):
        
        while True: 
            if self.seq.isOpen() == True:  
                try:
                    if self.seq.inWaiting():
                        try:
                            
                            self.command = self.seq.readline()
                            cmd_dec = self.command.decode()
                            cmd_sub = cmd_dec[:(len(cmd_dec)-2)]
                            if cmd_sub[0] == 'a':
                                a = cmd_sub.index('a')
                                b = cmd_sub.index('b')
                                c = cmd_sub.index('c')
                                d = cmd_sub.index('d')
                                e = cmd_sub.index('e')
                                temperature = float(cmd_sub[a+1:b])
                                humidity = float(cmd_sub[b+1:c])
                                distance  = float(cmd_sub[c+1:d])
                                light = int(cmd_sub[d+1:e])
                                print(temperature, humidity, distance, light)
                         
                        except AttributeError:
                            print("attr error")

                        
                except IOError:
                    print("IO error")

    def open_port(self):
        if self.seq.isOpen() == False:
            self.seq.open()

    def close_port(self):
        if self.seq.isOpen() == True:
            self.seq.close()

    def is_seq_open(self):
        if self.seq.isOpen() == True:
            return True
        else:
            return False

    def get_serial_port(self):
        return self.seq.port

    def get_serial_data(self):
        return self.command

if __name__ =='__main__':
    ser_manager = AiotSerialManager("/dev/ttyACM0")
    ser_manager.open_port()
    ser_manager.running()