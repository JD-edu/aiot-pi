from flask import Flask, render_template
from serial_class_can import SerialManager

app = Flask(__name__)

@app.route('/')
def hello():
    return("hello")

if __name__ == '__main__':
    ser_manager = AiotSerialManager("COM20")  # put your COM port number 
    ser_manager.open_port()
    ser_manager.start()
    app.run(port=5000, debug=False)
