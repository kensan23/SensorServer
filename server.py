#!/usr/bin/python3
from flask import Flask, Response
from flask_restful import Api
import Adafruit_DHT

application = Flask(__name__)
api = Api(app)

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

@app.route("/humidity", methods=['GET']) 
def humidity():
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        if humidity is not None and temperature is not None:
                return Response("{0:.2f}".format(humidity), status=200, mimetype='text/plain')
        else:
                return "Failed to retrieve data from humidity sensor", 503
@app.route("/temperature", methods=['GET']) 
def temperature():
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        if humidity is not None and temperature is not None:
                return Response("{0:0.1f}".format(temperature), status=200, mimetype='text/plain')
        else:
                return "Failed to retrieve data from temperature sensor", 503

if __name__ == '__main__':
        app.run(host='0.0.0.0')



    