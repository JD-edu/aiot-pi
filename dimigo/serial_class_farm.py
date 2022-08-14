#-*- coding:utf-8 -*-
import serial 
import time
from threading import Thread

class SerialManager(Thread):
   
    def __init__(self, serial_port):
        Thread.__init__(self)
        self.seq = serial.Serial(
            baudrate=115200,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
        )
        self.seq.port = serial_port
        self.daemon = True
        self.temperature = 0
        self.humidity = 0
        self.distance = 0
        self.light = 0
       
    def run(self):
        
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
                                self.temperature = float(cmd_sub[a+1:b])
                                self.humidity = float(cmd_sub[b+1:c])
                                self.distance  = float(cmd_sub[c+1:d])
                                self.light = int(cmd_sub[d+1:e])
                                print(self.temperature, self.humidity, self.distance, self.light)
                         
                        except ValueError:
                            print("value error")
                            
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
    
    def get_temp(self):
        return self.temperature
    
    def get_humid(self):
        return self.humidity
    
    def get_light(self):
        return self.light
    
    def get_distance(self):
        return self.distance

if __name__ =='__main__':
    ser_manager = SerialManager("COM20")
    ser_manager.open_port()
    ser_manager.run()
