import MidiProcessor
from collections import defaultdict
import time
#import RPi.GPIO as GPIO


class Actuator_Controller:
    def __init__(self,MIDIFile,delay=1):
        self.timeline=MidiProcessor.parseMidi(MIDIFile)
        self.delay=delay
        self.pause=False
        
         
        self.noteToPin = {'C':12,
            'C#':13,
            'D':5,
            'D#':6,
            'E':16,
            'F':18,
            'F#':19,
            'G':22,
            'G#':23,
            'A':24,
            'A#':25,
            'B':26}
        
        self.control_array=self.get_control_array()
      
    def get_control_array(self):
        grouped_events = defaultdict(lambda: {'wait': 0, 'notes_1': [], 'notes_0': []})
        for time, wait, event in self.timeline:
            grouped_events[time]['wait'] = max(grouped_events[time]['wait'], wait)
            if event.event_type == 1 and self.noteToPin[event.key.note[0]] not in grouped_events[time]['notes_1']:
                grouped_events[time]['notes_1'].append(self.noteToPin[event.key.note[0]])
            elif event.event_type == 0 and self.noteToPin[event.key.note[0]] not in grouped_events[time]['notes_0']:
                grouped_events[time]['notes_0'].append(self.noteToPin[event.key.note[0]])

        # Convert dictionary to list of tuples as required
        sorted_grouped_events = sorted(grouped_events.items())
        return [(time, info['wait'], info['notes_1'], info['notes_0']) for time, info in sorted_grouped_events]
    
    def Actuator_play(self):
        
        
        for t,wait,Highpins,Lowpins in self.control_array:

            if self.pause==True:
                while self.pause==True:
                    pass
            else:

            #GPIO.output(Highpins, GPIO.HIGH)
                print('GPIO HIGH:', Highpins)
           
            #GPIO.output(Lowpins, GPIO.LOW)
                print('GPIO LOW:',Lowpins)

                time.sleep((wait/1000)*self.delay)

    def play_pause(self):
        self.pause=True

    def play_continue(self):
        self.pause=False

    def test(self):
        test_array=self.noteToPin.values()
        for pins in test_array:
            #GPIO.Output(pins,GPIO.HIGH)
            print(pins)
            time.sleep(0.5)
            #GPIO.Output(pins,GPIO.LOW)
            print(pins)
        #GPIO.Output(test_array,GPIO.HIGH)
        print(test_array)
        time.sleep(0.3)
        #GPIO.Output(test_array,GPIO.LOW)
        




        


