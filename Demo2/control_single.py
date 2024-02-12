import RPi.GPIO as GPIO  
import time  # Import the time library for creating delays

# Global variable to track the pressed state
notePressed = False

def motorRunner(Mpin, onTime, offTime):
    global notePressed  # Declare the global variable to modify it within the function
    
    GPIO.setmode(GPIO.BCM)  # Set the GPIO pin numbering scheme to BCM
    GPIO.setup(Mpin, GPIO.OUT)  # Set the motor pin as an output pin

    if not notePressed:  # Check if the note is not already pressed
        notePressed = True 
        GPIO.output(Mpin, GPIO.HIGH)  # Turn on the motor (activate the actuator)
        time.sleep(onTime)  # Keep the motor on for the specified duration
        GPIO.output(Mpin, GPIO.LOW)  # Turn off the motor (deactivate the actuator)
        time.sleep(offTime)  # Wait for the specified duration before the next cycle
        resetNotePressed()

def resetNotePressed():
    global notePressed
    notePressed = False  # Reset the notePressed state for the next operation

# Example usage
motorPin = 12  # Motor GPIO pin number
onTime = 1  # Motor on time in seconds
offTime = 5  # Motor off time in seconds

try:
    while notePressed == False:
        motorRunner(motorPin, onTime, offTime)

except KeyboardInterrupt:  # Catch the Ctrl+C signal to exit the loop
    GPIO.cleanup()  # Clean up the GPIO pins before exiting

