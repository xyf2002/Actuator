"""
A python script that takes a midi file and converts it to a timeline of notes being played
"""
import mido 

MIDI_FILE = 'Marriagedamour.mid'

class Key:
    def __init__(self, key_num):
        self.original_key_num = key_num
        self.key_num = self.translate_to_61keys(key_num) - 12 
        self.note = self.get_note()

    def get_note(self):
        note = self.key_num % 12
        octave = self.key_num // 12
        notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        return notes[note] + str(octave)
    
    def translate_to_61keys(self, key_num):
        key = key_num
        while key > 96:
            key -= 12
        while key < 36:
            key += 12
        return key 
    
class KeyEvent: 

    def __init__(self, key, event_type):
        self.key = key
        self.event_type = event_type

def parseTrack(track):
    timeline = []
    current_time = 0

    for msg in track:
        current_time += msg.time
        if msg.type in ['note_on', 'note_off']:
            key = Key(msg.note)
            event_type = 1 if msg.type == 'note_on' and msg.velocity != 0 else 0
            event = KeyEvent(key, event_type)
            timeline.append((current_time, event))

    return timeline


def parseMidi(midi_file):
    mid = mido.MidiFile(midi_file)
    combined_timeline = [event for track in mid.tracks for event in parseTrack(track) if track]
    combined_timeline.sort(key=lambda x: x[0])

    # add wait times to the timeline
    wait_times = []
    for i in range(len(combined_timeline) - 1):
        wait_time = combined_timeline[i + 1][0] - combined_timeline[i][0]
        wait_times.append(wait_time)
    wait_times.append(0)  # no wait time for the last event
    combined_timeline = [(time, wait, event) for (time, event), wait in zip(combined_timeline, wait_times)]
    return combined_timeline    



def main():
    timeline = parseMidi(MIDI_FILE)
    for time, wait, event in timeline:
        pass
        #print(time, wait, event.key.note, event.key.key_num, event.event_type)
if __name__ == '__main__':
    main()
 




