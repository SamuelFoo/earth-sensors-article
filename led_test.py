import RPi.GPIO as GPIO
import time

# Pin configuration
LED_PIN = 18  # Set the GPIO pin you have connected the LED to

# Set up GPIO mode and pin
GPIO.setmode(GPIO.BCM)  # Use Broadcom (BCM) pin numbering
GPIO.setup(LED_PIN, GPIO.OUT)  # Set the LED pin as an output

# Blink the LED in a loop
try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)  # Turn on the LED
        time.sleep(5)  # Wait for 1 second
        GPIO.output(LED_PIN, GPIO.LOW)  # Turn off the LED
        time.sleep(5)  # Wait for 1 second

# Clean up GPIO settings on exit
except KeyboardInterrupt:
    print("Exiting program")
finally:
    GPIO.cleanup()  # Clean up GPIO configuration

