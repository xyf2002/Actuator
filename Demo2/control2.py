import RPi.GPIO as GPIO
import time

# 设置GPIO编号模式
GPIO.setmode(GPIO.BCM)

# 定义连接到直线电机的四个GPIO引脚
motorPins = [12, 5, 16, 18]

# 将这四个引脚全部设置为输出模式，并初始化为低电平（关闭状态）
for pin in motorPins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

try:
    while True:
        # 示例：顺序激活每个直线电机
        for pin in motorPins:
            GPIO.output(pin, GPIO.HIGH)  # 开启电机
            time.sleep(1)  # 电机工作1秒
            GPIO.output(pin, GPIO.LOW)   # 关闭电机
            time.sleep(1)  # 电机停止1秒之后再切换到下一个
        
        # 根据需要添加更多控制逻辑

except KeyboardInterrupt:
    # 清理GPIO设置
    GPIO.cleanup()
