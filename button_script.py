import RPi.GPIO as GPIO
import time
import subprocess

# Set up GPIO
BUTTON_PIN = 17
LED_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_PIN, GPIO.OUT)

# Variables to track script state
process = None

def start_script():
    global process
    if process is None:
        print("Starting script...")
        process = subprocess.Popen(["python3", "/home/pi/earth-sensors-article/simple_measurement.py"])  # Adjust the path to your script
    else:
        print("Script is already running.")

def stop_script():
    global process
    if process is not None:
        print("Stopping script...")
        process.terminate()
        process = None
    else:
        print("Script is not running.")

try:
    while True:
        button_state = GPIO.input(BUTTON_PIN)
        if button_state == GPIO.LOW:  # Button is pressed
            if process is None:
                GPIO.output(LED_PIN, GPIO.HIGH)  # Turn on the LED
                start_script()
            else:
                GPIO.output(LED_PIN, GPIO.LOW)
                stop_script()
            time.sleep(1)  # Debounce delay
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Exiting program")

finally:
    GPIO.cleanup()

