#import RPi.GPIO as GPIO
import time
import threading  # 导入线程库
import MidiProcessor
from Actuator_Controller import Actuator_Controller

midi='HappyBirthday.mid'
controller=Actuator_Controller(midi,10)
controller.test()

'''
GPIO.setmode(GPIO.BCM)  # Set GPIO mode to BCM
motorPins=[]

# 全局变量，跟踪按键状态
notePressed = False

# 初始化GPIO引脚
def setupGPIO():
    for pin in motorPins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)

'''
'''
noteToPin = {'C':12,
            'D':5,
            'E':16,
            'F':18,
            'G':22,
            'A':24,
            'B':26}
'''



'''
def getActArray(MIDIFILE):
    
    grouped_notes = {}
    for event in note_events:
        start_time, ontime, Keyevent= event
        if Keyevent.event_type == 1:  # Note start
            if start_time not in grouped_notes:
                grouped_notes[start_time] = [note_name]
            else:
                grouped_notes[start_time].append(note_name)
    
    # Convert the dictionary to a sorted list of tuples
    sorted_grouped_notes = sorted(grouped_notes.items())
    return sorted_grouped_notes



        



# 单个电机运行函数
def motorRunner(infSet):
    GPIO.output(infSet[0], GPIO.HIGH)
    time.sleep(infSet[1])
    GPIO.output(infSet[0], GPIO.LOW)
    
#Do:12 Re:5 Mi:16 Fa:18 So:22 La:24 Si:26
Joy=[[16,0.5,0],[16,0.5,0],[18,0.5,0],[22,0.5,0],[22,0.5,0],[18,0.5,0],[16,0.5,0],[5,0.5,0],[12,0.5,0],[12,0.5,0],[5,0.5,0],[16,0.5,0],[16,0.75,0][5,0.25,0][5,1,0]]
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
        '''