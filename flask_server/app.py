from flask import Flask
from flask import Flask, render_template, Response, make_response, jsonify
import numpy as np

import json
import pandas
import numpy as np

app = Flask(__name__)


sensors = {'sensor1':[120, 14, 3, 2], 'temp1':[25,23,20], 'humidity':[30, 40, 50]}


d = [{"x":0, "y":0}, {"x":1, "y":1}]


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

@app.route('/streamdata')
def event_stream():
    # ici get new data from database
    last_y = d[-1]['y']
    last_x = d[-1]['x']
    d.append({"x":last_x+10, "y":np.random.randint(5)})
    print("Stream data %s" % d)
    #return make_response(data=json.dumps(d))
    return make_response(json.dumps(d))
    #res = jsonify(result=d)
    #return make_response(res)
    #print("res is %s" % res)
    #print(res.__dict__)
    #return res

@app.route('/stream')
def show_basic():
    return render_template("visualization_live.html")


if __name__ == '__main__':
    app.run(debug=True)
