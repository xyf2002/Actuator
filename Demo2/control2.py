import RPi.GPIO as GPIO
import time

# Global variable to track the activation state
notePressed = False

# Setup GPIO
GPIO.setmode(GPIO.BCM)

# Define motor pins
motorPins = [12, 5, 16, 18]

# Set all pins as output and initialize to low
for pin in motorPins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

def motorRunner(mpins, onTime, offTime):
    global notePressed
    
    if not notePressed:
        notePressed = True
        # Activate two motors simultaneously
        for Mpin in mpins:
            GPIO.output(Mpin, GPIO.HIGH)
        time.sleep(onTime)
        for Mpin in mpins:
            GPIO.output(Mpin, GPIO.LOW)
        time.sleep(offTime)
        notePressed = False

try:
    while True:
        # Check if the note is not pressed and activate two motors
        if not notePressed:
            # Example: Activate first two motors together, then next two
            motorRunner(motorPins[:2], 1, 1)  # Activates pins 12 and 5 together
            motorRunner(motorPins[2:], 1, 1)  # Activates pins 16 and 18 together

except KeyboardInterrupt:
    GPIO.cleanup()  # Cleanup GPIO setup on Ctrl+C
