from flask import Flask
import numpy as np


app = Flask(__name__)


sensors = {'sensor1':[120, 14, 3, 2], 'temp1':[25,23,20], 'humidity':[30, 40, 50]}

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/sensor/<sensor_name>')
def get_sensor(sensor_name):
    key = sensor_name
    return str(sensors[key])


@app.route('/sensor/<sensor_name>/mean')
def get_sensor_mean(sensor_name):
    key = sensor_name
    mean = np.mean(sensors[key])
    return str(mean)


if __name__ == '__main__':
    app.run(debug=True)
