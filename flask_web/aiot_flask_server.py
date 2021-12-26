from flask import Flask, render_template
from aiot_arduino_serial_class_thread import AiotSerialManager

app = Flask(__name__)

@app.route('/')
def hello():
    return("hello")

@app.route('/method', methods=['GET', 'POST'])
def method():
    temp = ser_manager.get_temp()
    humid = ser_manager.get_humid()
    light = ser_manager.get_light()
    distance = ser_manager.get_distance()
    templateData = {
        'temp' : temp,
        'humid' : humid,
        'light' : light,
        'distance': distance
        }
    return render_template('index.html', **templateData)

if __name__ == '__main__':
    ser_manager = AiotSerialManager("/dev/ttyACM0")
    ser_manager.start()
    ser_manager.open_port()
    app.run(port=5000, debug=True)