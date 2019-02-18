#!/usr/bin/python

import os
import pyowm

try:
    apikey = os.environ['OPENWEATHER_API_KEY']
except:
    print("\r\nPlease set the OPENWEATHER_API_KEY variable")
    print("Run 'export OPENWEATHER_API_KEY=<your api key>' \r\n")
    exit()

try:
    cityname = os.environ['CITY_NAME']
except:
    print("\r\nPlease set the CITY_NAME variable")
    print("Run 'export CITY_NAME=<Name of the city>' \r\n")
    exit()

owm = pyowm.OWM(apikey)

try:
    weathersensor = owm.weather_at_place(cityname)
except Exception as e:
    print(e)
    exit()

weatherdata = weathersensor.get_weather()
locationdata = weathersensor.get_location()

dict = {
    "source": "openweathermap",
    "city": locationdata.get_name(),
    "description": weatherdata.get_detailed_status(),
    "temp": weatherdata.get_temperature('fahrenheit')['temp'],
    "humidity":  weatherdata.get_humidity()
}

print ('source=%s, city="%s", description="%s", temp=%s, humidity=%s' % 
          (dict["source"], dict["city"], dict["description"], dict["temp"], dict["humidity"]))
