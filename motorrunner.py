import RPi.GPIO as GPIO
import time
import threading  # 导入线程库

GPIO.setmode(GPIO.BCM)  # 设置GPIO编号模式为BCM

# 定义连接到直线电机的GPIO引脚
motorPins = [12, 5, 16, 18]

# 全局变量，跟踪按键状态
notePressed = False

# 初始化GPIO引脚
def setupGPIO():
    for pin in motorPins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)

# 单个电机运行函数
def motorRunner(mpin, onTime, offTime):
    GPIO.output(mpin, GPIO.HIGH)
    time.sleep(onTime)
    GPIO.output(mpin, GPIO.LOW)
    time.sleep(offTime)


# 主程序
if __name__ == "__main__":
    setupGPIO()
    
    try:
        while True:
            if not notePressed:
                notePressed = True  # 更新按键状态
                # 同时激活所有电机
                motorRunner(motorPins[:2], 1, 1)  # 例如，激活前两个电机
                time.sleep(2)  # 休息一段时间后再次检查
                notePressed = False  # 重置按键状态，准备下一次激活

    except KeyboardInterrupt:
        GPIO.cleanup()  # 清理GPIO设置