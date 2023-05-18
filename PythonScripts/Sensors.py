# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from sense_hat import SenseHat
import json
import os

sense = SenseHat()

sense.set_imu_config(True, True, True)



orientation = sense.get_orientation_degrees()
humidity = sense.get_humidity()
temp = sense.get_temperature()
pressure = sense.get_pressure()
north = sense.get_compass()
gyro_only = sense.get_gyroscope()
accel_only = sense.get_accelerometer()

json_data ={
    'orientation': orientation,
    'humidity': humidity,
    'temp': temp,
    'pressure': pressure,
    'north': north,
    'gyro_only': gyro_only,
    'accel_only': accel_only,    
    }

path = os.path.join("/home/safeharbourtech/ApplicationCode/DataSender", "sensor_data.json" )
with open(path, "w", encoding='utf-8') as fp:
    json.dump(json_data, fp, sort_keys=True, indent=4)

#sense.show_message("SAFE HARBOUR TECH!")
#sense.show_message("Temperature: %.2f C" % temp, text_colour=[255,0,0])
