# raspberry_pi.py
from flask import Flask
from flask_socketio import SocketIO
import RPi.GPIO as GPIO

app = Flask(__name__)
socketio = SocketIO(app)

motorPin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(motorPin, GPIO.OUT)

@socketio.on('control_motor')
def handle_motor_control(message):
    if message['action'] == 'on':
        GPIO.output(motorPin, GPIO.HIGH)
    elif message['action'] == 'off':
        GPIO.output(motorPin, GPIO.LOW)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8080)
