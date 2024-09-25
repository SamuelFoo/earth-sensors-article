# Setup of Raspberry Pi and Carbon Dioxide + BME688 Sensor. 

NOTE : Major changes are upcoming

Instructions to setting up Raspberry Pi to [K30 10,000 ppm Carbon Dioxide Sensor](https://www.co2meter.com/products/k-30-co2-sensor-module), can be found in `setup-manual.pdf`. Additional python code files used are also provided to parse readings and save them to an output file. 

Instructions for setting up Adafruit BME688 sensor :

[https://learn.adafruit.com/adafruit-bme680-humidity-temperature-barometic-pressure-voc-gas/python-circuitpython](https://learn.adafruit.com/adafruit-bme680-humidity-temperature-barometic-pressure-voc-gas/python-circuitpython)

To setup a the Raspbery Pi to work with the sensors, prepare a fresh copy of Raspberry Pi OS, and clone this repository into the home directory, then run the `setup.sh` script within the repo.

## Setup GCloud Bucket Storage

### Install GCloud CLI

See https://cloud.google.com/sdk/docs/install#deb

### Create Bucket

See https://cloud.google.com/storage/docs/creating-buckets#console

Edit the `command` variable in `simple_measurement.py` to use the name of the created bucket. 

## Set up crontab

```
crontab -e
```

## Wiring

Button to GPIO 17.
LED to GPIO 18.

## Pathing

Don't rename this directory. Place in `/home/pi`.
