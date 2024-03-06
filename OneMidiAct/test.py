import MidiProcessor
import motorrunner
import Timer
from collections import defaultdict
'''
def group_events_by_time(timeline):
    grouped_events = defaultdict(lambda: {'wait': 0, 'notes_1': [], 'notes_0': []})
    for time, wait, event in timeline:
        grouped_events[time]['wait'] = max(grouped_events[time]['wait'], wait)
        if event.event_type == 1:
            grouped_events[time]['notes_1'].append(event.key.note)
        else:
            grouped_events[time]['notes_0'].append(event.key.note)

    # Convert dictionary to list of tuples as required
    sorted_grouped_events = sorted(grouped_events.items())
    return [(time, info['wait'], info['notes_1'], info['notes_0']) for time, info in sorted_grouped_events]

'''
'''
from collections import defaultdict

def group_events_by_time(timeline):
    grouped_events = defaultdict(lambda: {'wait': 0, 'events_1': [], 'events_0': []})
    for time, wait, event in timeline:
        grouped_events[time]['wait'] = max(grouped_events[time]['wait'], wait)
        if event.event_type == 1:
            grouped_events[time]['events_1'].append(event)
        else:
            grouped_events[time]['events_0'].append(event)

    # Convert dictionary to list of tuples as required
    sorted_grouped_events = sorted(grouped_events.items())
    return [(time, info['wait'], info['events_1'], info['events_0']) for time, info in sorted_grouped_events]
'''
'''
def group_notes_by_start_time(MIDI):
    
    """
    Groups notes that are played at the same time into tuples.

    Args:
        note_events (list of tuples/lists): Each element contains attributes of the note event:
            [start time, duration, note name, numerical value, flag indicating start/end (1/0)].

    Returns:
        list of tuples: Each tuple contains the start time and a list of note names that start at that time.
    """
    note_events = MidiProcessor.parseMidi(MIDI)
    grouped_notes = {}
   
    for event in note_events:
        start_time, _, Keyevent= event
        pin=motorrunner.noteToPin[Keyevent.key.note[0]]
        if Keyevent.event_type == 1:  # Note start
            if start_time not in grouped_notes:
                grouped_notes[start_time] = [pin]
            elif pin not in grouped_notes[start_time]:
                grouped_notes[start_time].append(pin)
    
    # Convert the dictionary to a sorted list of tuples
    sorted_grouped_notes = sorted(grouped_notes.items())
    return sorted_grouped_notes

'''
'''
midi='HappyBirthday.mid'
timelinr=group_events_by_time(MidiProcessor.parseMidi(midi))
for time,wait,event_1,event_0 in timelinr:
    print(time,wait,event_1,event_0)
'''
'''


# Test the function with the provided data



def timer():
    startTime=time.time_ns()//1000000
    while True:
        CurrentTime=time.time_ns()//1000000
        Duration=CurrentTime-startTime
        return Duration



while True:
    time=Timer.get_time()
    if time==2000:
        print('time')




def create_timer():
    start_time = time.time_ns() // 1000000  # Store the start time when the function is created
    
    def timer():
        # This inner function calculates the time elapsed since `start_time` in milliseconds
        return time.time_ns() // 1000000 - start_time
    
    return timer

# Create a timer instance outside the loop
timer = create_timer()
print("Timer started.")

while True:
    #elapsed_time = timer()  # Get the elapsed time by calling the timer
    #print(f"Elapsed time: {elapsed_time} ms")  # Print the current elapsed time for debugging
    if elapsed_time >= 2000:  # Check if 2000 milliseconds have passed
        print('2 seconds have passed')
        # Exit the loop
      # Adjust this for more frequent checks without
      '''
      