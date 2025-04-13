#%%
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavf
from scipy import fftpack
import winsound, json

sound_name = 'music.wav'

##-------------------------------------FUNCTIONS-------------------------------------

def saveWav(file, signal, samplerate, amplify=1, speed_up=1, playWav=False):
    try: wavf.write(file, int(speed_up* samplerate), amplify* signal.astype(np.int16))
    except Exception as ex: print(ex)
    if playWav: winsound.PlaySound(file, winsound.SND_FILENAME)

def fourier(data, samplerate, signal_name='x1', plotSignals=True):
    N_s = data.shape[0] # Number of samplepoints
    duration = N_s / samplerate #Total time in sec

    x = data
    t = np.linspace(0, duration, N_s)
    X = fftpack.fft(x)
    freqs = fftpack.fftfreq(data.shape[0]) *samplerate
    
    if plotSignals:
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

##-------------------------------------MAIN PROGRAM-------------------------------------
samplerate, data =  wavf.read(sound_name) #Samplerate (Fs) == 44.1 kHz

if data.shape[1]>1: data = data[:,0]
X1, freqs = fourier(data, samplerate)

#Save in Json:
json.dump(data.tolist(), open("datafile.txt", 'w'), separators=(',', ':'), sort_keys=True, indent=4)
#data.tofile('datatestfile.json') or data.dump('datas.json')


