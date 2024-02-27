import RPi.GPIO as GPIO
import time
import threading  # 导入线程库


GPIO.setmode(GPIO.BCM)  # 设置GPIO编号模式为BCM

# 定义连接到直线电机的GPIO引脚
motorPins = [12, 5, 16, 18，22, 24，26]

# 全局变量，跟踪按键状态
notePressed = False

# 初始化GPIO引脚
def setupGPIO():
    for pin in motorPins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)

# 单个电机运行函数
def motorRunner(infSet):
    GPIO.output(infSet[0], GPIO.HIGH)
    time.sleep(infSet[1])
    GPIO.output(infSet[0], GPIO.LOW)
    time.sleep(infSet[2])
#Do:12 Re:5 Mi:16 Fa:18 So:22 La:24 Si:26

Joy=[[16,0.5,0],[16,0.5,0],[18,0.5,0],[22,0.5,0],[22,0.5,0],[18,0.5,0],[16,0.5,0],[5,0.5,0],[12,0.5,0],[12,0.5,0],[5,0.5,0],[16,0.5,0],[16,0.75,0],[5,0.25,0],[5,1,0]]
DoToSi=[[12,0.25,0.1],[12,0.5,0],[5,0.25,0.1],[5,0.5,0],[16,0.25,0.1],[16,0.5,0],[18,0.25,0.1],[18,0.5,0],[22,0.25,0.1],[22,0.5,0],[24,0.25,0.1],[24,0.5,0],[26,0.25,0.1],[26,0.5,0]]
# 主程序
if __name__ == "__main__":
    setupGPIO()
    
    try:
        for infset in Joy:
            if not notePressed:
                notePressed = True  # 更新按键状态
                # 同时激活所有电机
                motorRunner(infset)  # 例如，激活前两个电机
                 # 休息一段时间后再次检查
                notePressed = False  # 重置按键状态，准备下一次激活

    

    except KeyboardInterrupt:
        GPIO.cleanup()  # 清理GPIO设置