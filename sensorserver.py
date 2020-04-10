#!/usr/bin/python3
from flask import Flask, Response
from flask_restful import Api
import bme680
import json

application = Flask(__name__)
api = Api(application)
try:
    sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
except IOError:
    sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)
sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)

@application.route("api/v1/live/humidity", methods=['GET']) 
def humidity():
        if sensor.get_sensor_data():
                return json.dumps('{2:.2f}'.format(sensor.data.humidity));
        else:
                return "Sensor error", 503
@application.route("/api/v1/live/temperature", methods=['GET']) 
def temperature():
        if sensor.get_sensor_data():
                return json.dumps('{0:.2f} C'.format(sensor.data.temperature));
        else:
                return "Sensor error", 503
@application.route("/api/v1/live/pressure", methods=['GET']) 
def temperature():
        if sensor.get_sensor_data():
                return json.dumps('{1:.2f} hPa'.format(sensor.data.pressure));
        else:
                return "Sensor error", 503
@application.route("/api/v1/live/", methods=['GET']) 
def getAll():
        humidity = 300;
        if humidity is not None and temperature is not None:
                return Response(json.dumps(response), status=200, mimetype='application/json')
        else:
                return "Failed to retrieve data from dht22", 503

if __name__ == '__main__':
        application.run()



