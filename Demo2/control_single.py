import RPi.GPIO as GPIO  # Import the GPIO library for controlling the GPIO pins of the Raspberry Pi
import time  # Import the time library for creating delays

def motorRunner(Mpin, onTime, offTime):
    """
    Controls a motor connected to a specified GPIO pin by turning it on for a given duration,
    then off for a given duration, in a continuous loop.

    Parameters:
    - Mpin: GPIO pin number to which the motor is connected.
    - onTime: Duration (in seconds) the motor remains on.
    - offTime: Duration (in seconds) the motor remains off before the next cycle.
    """
    GPIO.setmode(GPIO.BCM)  # Set the GPIO pin numbering scheme to BCM

    # Set the motor pin as an output pin
    GPIO.setup(Mpin, GPIO.OUT)

    try:
        while True:  # Create an infinite loop to continuously operate the motor
            GPIO.output(Mpin, GPIO.HIGH)  # Turn on the motor (activate the actuator)
            time.sleep(onTime)  # Keep the motor on for the specified duration
            GPIO.output(Mpin, GPIO.LOW)  # Turn off the motor (deactivate the actuator)
            time.sleep(offTime)  # Wait for the specified duration before the next cycle

    except KeyboardInterrupt:  # Catch the Ctrl+C signal to exit the loop
        GPIO.cleanup()  # Clean up the GPIO pins before exiting

# Example usage
motorPin = 18  # Assign the GPIO pin number that the linear motor is connected to
onTime = 1  # Motor on time in seconds
offTime = 5  # Motor off time in seconds

# Call the function with the motor pin, on time, and off time
motorRunner(motorPin, onTime, offTime)

