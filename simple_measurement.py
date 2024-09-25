#!/usr/bin/python3
import csv
import time
from pathlib import Path
from sensors import connect_to_CO2_sensor, get_CO2_reading, connect_to_bme688_sensor
from datetime import datetime
import sys
import signal

import subprocess

def signal_handler(sig, frame):
    print('Uploading file')
    command = f"/usr/bin/gsutil cp '{str(OUTPUT_FILE.absolute())}' gs://co2-measurements-pi-3"
    subprocess.call(command, shell=True)
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

OUTPUT_FILE = Path(f"/home/pi/earth-sensors-article/readings/{datetime.now()}.csv")

if not OUTPUT_FILE.exists():
	with open(OUTPUT_FILE, mode = "a", buffering = 1) as csvfile:
		csv_writer = csv.writer(csvfile)
		csv_writer.writerow(("Time", "CO2", "Temperature", "Humidity", "Pressure", "Gas"))

with open(OUTPUT_FILE, mode = "a", buffering = 1) as csvfile:
    csv_writer = csv.writer(csvfile)
    CO2_sensor = connect_to_CO2_sensor()
    bme688_sensor = connect_to_bme688_sensor()

    start_time = time.time()
    while True:
        CO2 = get_CO2_reading(CO2_sensor)
        temp = bme688_sensor.temperature
        hum = bme688_sensor.relative_humidity
        pressure = bme688_sensor.pressure
        gas = bme688_sensor.gas
        print(f"CO2: {CO2}, T: {temp}, H: {hum}, P: {pressure}, G: {gas}")
        csv_writer.writerow((time.time() - start_time, CO2, temp, hum, pressure, gas))
        csvfile.flush()

