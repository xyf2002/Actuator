import RPi.GPIO as GPIO  # Import the GPIO library for controlling the GPIO pins of the Raspberry Pi
import time  # Import the time library for creating delays

GPIO.setmode(GPIO.BCM)  # Set the GPIO pin numbering scheme to BCM

motorPin = 18  # Assign the GPIO pin number that the linear motor is connected to

# Set the motor pin as an output pin
GPIO.setup(motorPin, GPIO.OUT)

try:
    while True:  # Create an infinite loop to continuously operate the motor
        GPIO.output(motorPin, GPIO.HIGH)  # Turn on the motor (activate the actuator)
        time.sleep(1)  # Keep the motor on for 1 second
        GPIO.output(motorPin, GPIO.LOW)  # Turn off the motor (deactivate the actuator)
        time.sleep(5)  # Wait for 5 seconds before the next cycle

except KeyboardInterrupt:  # Catch the Ctrl+C signal to exit the loop
    GPIO.cleanup()  # Clean up the GPIO pins before exiting
