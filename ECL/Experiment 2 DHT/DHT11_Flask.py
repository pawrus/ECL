from flask import Flask, render_template, jsonify
import Adafruit_DHT


app = Flask(__name__)


DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 17 

def get_sensor_data():
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)  
    if humidity is not None and temperature is not None:
        return {'temperature': temperature, 'humidity': humidity}
    else:
        return {'temperature': None, 'humidity': None}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sensor-data')
def sensor_data():
    data = get_sensor_data()
    return jsonify(data)  

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
