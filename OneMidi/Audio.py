import time
import pygame
from MidiProcessor import parseMidi

DIRECTORY = 'audio'
#MIDI_FILE = 'HappyBirthday.mid'
MIDI_FILE = 'Marriagedamour.mid'

pygame.mixer.init()
sounds = {}  # Dictionary to hold sound objects

def load_sounds(directory):
    """Load piano note sounds from files into a dictionary."""
    # Adjusted to handle unique naming scheme and octaves
    full_octave_note_names = ['c', 'cs', 'd', 'ds', 'e', 'f', 'fs', 'g', 'gs', 'a', 'as', 'b']
    for note in range(21, 108 ): #Changed the range to 108 not 109 as there is no 108 sound. 
        octave = (note - 12) // 12
        note_name = full_octave_note_names[(note - 21) % 12] if note > 23 else ['a', 'as', 'b'][note - 21]
        sound_path = f"{directory}/{octave}-{note_name}.wav"
        try:
            sounds[note] = pygame.mixer.Sound(sound_path)
        except FileNotFoundError:
            print(f"Sound file for note {note} ({sound_path}) not found.")

def play_note(note):
    if note in sounds:
        sounds[note].play()

def stop_note(note):
    if note in sounds:
        sounds[note].stop()

def playMidi(midi_file, speed=1.0):
    load_sounds(DIRECTORY)  # Ensure this directory exists and contains the WAV files
    timeline = parseMidi(midi_file)
    for event_time, wait, event in timeline:
        print(event_time, wait, event.key.note, event.key.key_num, event.event_type)
        if event.event_type == 1:
            play_note(event.key.key_num)
        else:
            stop_note(event.key.key_num)
        time.sleep(wait/(speed*1000))  # sleep for the duration of the note

playMidi(MIDI_FILE, 0.2)  
