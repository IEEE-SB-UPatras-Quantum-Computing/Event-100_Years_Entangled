# %%
from random import randint
from matplotlib import pyplot as plt

bits = ''

for i in range(100_000):
    bits += str(randint(0,1))

zeros_counts = {}

for i in range(10):
    seq = '0'*i
    count = bits.count(f'1{seq}1')
    zeros_counts[seq] = count
for i in range(10):
    seq = '1'*i
    count = bits.count(f'0{seq}0')
    zeros_counts[seq] = count

plt.bar(zeros_counts.keys(), zeros_counts.values())

# %%
from matplotlib import pyplot as plt
import numpy as np
from scipy.io import wavfile
from scipy import fftpack

def saveWav(file, signal, samplerate, amplify=1, speed_up=1, playWav=False):
    wavfile.write(file, int(speed_up* samplerate), amplify* signal.astype(np.int16))

def fourier(data, samplerate, signal_name='x1', plotSignals=True):
    N_s = data.shape[0] # Number of samplepoints
    duration = N_s / samplerate #Total time in sec

    x = data
    X = fftpack.fft(x)
    freqs = fftpack.fftfreq(data.shape[0]) *samplerate
    
    if plotSignals:
        t = np.linspace(0, duration, N_s)

        #Signal Plot
        plt.subplot(2,1,1)
        plt.grid()
        plt.plot(t,x)
        plt.xlabel('Time[s]')
        plt.ylabel('Amplitude')
        plt.title('Time Domain -- '+signal_name.lower())

        #Fourier Plot
        plt.subplot(2,1,2)
        plt.grid()
        plt.plot(freqs, np.abs(X))
        plt.xlabel('Frequency[Hz]')
        plt.ylabel('Amplitude')
        plt.title('Frequency Domain -- '+signal_name.capitalize())

        plt.subplots_adjust(hspace=1)
        plt.show()

    return X, freqs


samplerate, data = wavfile.read("test.wav")
# data = data[:,1]
X, freqs = fourier(data, samplerate)


# %%
from scipy.io import wavfile
import numpy as np
from matplotlib import pyplot as plt


VOLUMN = 10_000
FREQUENCY = 261.626
DURATION = .5 # seconds
SEMITONE = np.pow(2,1/12)
TONE = SEMITONE**2
SAMPLERATE = 44100 # const

def create_note(frequency=FREQUENCY, volumn=VOLUMN):
    x = np.linspace(0, DURATION, int(SAMPLERATE*DURATION))
    y = np.sin(frequency*x)
    return volumn*y

do = create_note(FREQUENCY)
re = create_note(TONE*FREQUENCY)
mi = create_note(TONE**2*FREQUENCY)
fa = create_note(TONE**2*SEMITONE*FREQUENCY)
sol = create_note(TONE**3*SEMITONE*FREQUENCY)
la = create_note(TONE**4*SEMITONE*FREQUENCY)
si = create_note(TONE**5*SEMITONE*FREQUENCY)
do2 = create_note(2*FREQUENCY)

# d = np.append(do, [re,mi,fa,sol,la,si,do2])



wavfile.write("test.wav", SAMPLERATE, do2.astype(np.int16))


