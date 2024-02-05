from flask import Flask, render_template, request
import RPi.GPIO as GPIO

app = Flask(__name__)

motorPin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(motorPin, GPIO.OUT)

@app.route('/')
def index():
    return render_template('index.html')  # 提供一个包含控制按钮的HTML页面

@app.route('/control_motor', methods=['POST'])
def control_motor():
    action = request.form.get('action')
    if action == 'on':
        GPIO.output(motorPin, GPIO.HIGH)
    elif action == 'off':
        GPIO.output(motorPin, GPIO.LOW)
    return ('', 204)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)