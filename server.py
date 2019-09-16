#!/usr/bin/python3
from flask import Flask, Response
from flask_restful import Api
import Adafruit_DHT
import json

application = Flask(__name__)
api = Api(application)

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

@application.route("/humidity", methods=['GET']) 
def humidity():
        humidity = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)[0]
        if humidity is not None:
                return Response("{0:.2f}".format(humidity), status=200, mimetype='text/plain')
        else:
                return "Failed to retrieve data from dht22 sensor", 503
@application.route("/temperature", methods=['GET']) 
def temperature():
        temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)[1]
        if temperature is not None:
                return Response("{0:0.1f}".format(temperature), status=200, mimetype='text/plain')
        else:
                return "Failed to retrieve data dht22 sensor", 503

@application.route("/all", methods=['GET']) 
def getAll():
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        response = dict({"humidity":"{0:.2f}".format(humidity), "temperature":"{0:0.1f}".format(temperature)})

        if humidity is not None and temperature is not None:
                return Response(json.dumps(response), status=200, mimetype='application/json')
        else:
                return "Failed to retrieve data from dht22", 503

if __name__ == '__main__':
        application.run(host='0.0.0.0')



    