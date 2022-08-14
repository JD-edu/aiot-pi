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
       
    def run(self):
        
        while True: 
            if self.seq.isOpen() == True: 
                
                try:
                    if self.seq.inWaiting():
                        try:       
                            self.command = self.seq.readline()
                            print(self.command)
                            cmd_dec = self.command.decode()
                            # camera read -> inference -> servo command 
                            #self.seq.write("can\r\n")
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
    
if __name__ =='__main__':
    ser_manager = SerialManager("COM20")
    ser_manager.open_port()
    ser_manager.start()
