import MidiProcessor
from collections import defaultdict
import time
import RPi.GPIO as GPIO


class Actuator_Controller:
    def __init__(self,MIDIFile):
        self.timeline=MidiProcessor.parseMidi(MIDIFile)
         
        self.noteToPin = {'C':12,
            'D':5,
            'E':16,
            'F':18,
            'G':22,
            'A':24,
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

            GPIO.output(Highpins, GPIO.HIGH)
            #print('GPIO HIGH:', Highpins)
           
            GPIO.output(Lowpins, GPIO.LOW)
            #print('GPIO LOW:',Lowpins)

            time.sleep(wait/1000)



        


controller=Actuator_Controller('HappyBirthday.mid')
controller.Actuator_play()