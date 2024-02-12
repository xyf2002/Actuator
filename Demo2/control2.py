import RPi.GPIO as GPIO
import time
import threading  # 导入线程库

# 同前定义全局变量、GPIO设置和motorPins
# Define motor pins
motorPins = [12, 5, 16, 18]
notePressed = False

def motorRunner(mpin, onTime, offTime):
    GPIO.output(mpin, GPIO.HIGH)
    time.sleep(onTime)
    GPIO.output(mpin, GPIO.LOW)
    time.sleep(offTime)

def runMotorsSimultaneously(mpins, onTime, offTime):
    threads = []
    for pin in mpins:
        thread = threading.Thread(target=motorRunner, args=(pin, onTime, offTime))
        threads.append(thread)
        thread.start()
    
    # 等待所有线程完成
    for thread in threads:
        thread.join()

try:
    while True:
        if not notePressed:
            notePressed = True
            # 同时激活所有电机
            runMotorsSimultaneously(motorPins, 1, 1)
            notePressed = False

except KeyboardInterrupt:
    GPIO.cleanup()

