import RPi.GPIO as GPIO  
import time  

# Global variable to track the pressed state
notePressed = False

def motorRunner(Mpin, onTime, offTime):
    global notePressed  
    
    GPIO.setmode(GPIO.BCM)  
    GPIO.setup(Mpin, GPIO.OUT)  

    try:
        while True:  # Keep running the motor in an infinite loop
            if not notePressed:  # If the note is not pressed, activate the motor
                notePressed = True 
                GPIO.output(Mpin, GPIO.HIGH)  
                time.sleep(onTime)  
                GPIO.output(Mpin, GPIO.LOW)  
                time.sleep(offTime)  
                notePressed = False  # Reset the notePressed state for the next cycle
    except KeyboardInterrupt:  # Allow a keyboard interrupt to break the loop
        GPIO.cleanup()  # Clean up the GPIO pins before exiting

# Example usage
motorPin = 12  # Motor GPIO pin number
onTime = 1  # Motor on time in seconds
offTime = 1  # Motor off time in seconds

motorRunner(motorPin, onTime, offTime)  # Call the function to start the motor loop


