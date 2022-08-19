from flask import Flask, render_template
from serial_class_farm import SerialManager

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
    ser_manager = SerialManager("COM20")
    ser_manager.open_port()
    ser_manager.start()
    app.run(port=5000, debug=False)
