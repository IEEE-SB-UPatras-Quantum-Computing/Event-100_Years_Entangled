# %%
import numpy as np
from scipy.io import wavfile

FILE_NAME = "data.txt"
NOTE_SIZE = 3
VOLUMN = 10_000
SAMPLERATE = 44100 # const
FREQUENCY = 261.626 *5
DURATION = .5
SEMITONE = np.pow(2,1/12)
TONE = SEMITONE**2

def create_note(frequency=FREQUENCY, volumn=VOLUMN):
    x = np.linspace(0, DURATION, int(SAMPLERATE*DURATION))
    y = np.sin(frequency*x)
    return volumn*y

DO = create_note(FREQUENCY)
RE = create_note(TONE*FREQUENCY)
MI = create_note(TONE**2*FREQUENCY)
FA = create_note(TONE**2*SEMITONE*FREQUENCY)
SOL = create_note(TONE**3*SEMITONE*FREQUENCY)
LA = create_note(TONE**4*SEMITONE*FREQUENCY)
SI = create_note(TONE**5*SEMITONE*FREQUENCY)
DO2 = create_note(2*FREQUENCY)

NOTES = [DO,RE,MI,FA,SOL,LA,SI,DO2]


with open(FILE_NAME, "r") as f:
    data = f.read()

notes_len = len(data)//NOTE_SIZE
notes = []

for i in range(notes_len):
    datum = data[NOTE_SIZE*i : NOTE_SIZE*(i+1)]
    index = int(datum, 2)
    notes.append(NOTES[index])

d = np.append([], notes)

wavfile.write("sound.wav", SAMPLERATE, d.astype(np.int16))
