import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def calcAmp(data, fs):
    ''' Fourier transform and calculate amplitude
    '''
    num = len(data)
    window = signal.hanning(num) # hanning window
    ft = np.fft.fft(data*window)
    freq = np.fft.fftfreq(num, d=1./fs) # frequency scale
    ft = ft / (num / 2.) # normalization
    ft = ft * (num/ sum(window)) # compensate with window function
    amp = np.abs(ft) # amplitude of spectrum
    return amp, freq

def createDummy():
    num = 1024            # the number of samples
    dt = 0.0005         # sampling period [s]
    fs = 1 / dt         # sampling frequency [Hz]
    f1, f2, f3 = 30, 432, 604    # frequency of data and noize [Hz]

    t = np.arange(0, num * dt, dt) # time  [s]
    x = 1.5 * np.sin(2 * np.pi * f1 * t) \
        + 0.5 * np.sin(2 * np.pi * f2 * t) \
        + 0.7 * np.sin(2 * np.pi * f3 * t) # data
    
    return num, fs, x, t

def fromCSV():
    import pandas as pd
    df = pd.read_csv('../sample_data.csv', header=None)
    num = df.shape[0]
    dt = 0.025
    fs = 1./dt
    t = np.arange(0, num*dt, dt)
    x = np.zeros(num)
    x = df[1].values
    
    return num, fs, x, t
    
        
if __name__ == "__main__":
    # num, fs, x, t = createDummy()
    num, fs, x, t = fromCSV()
    amp, freq = calcAmp(x, fs)    
    fig, ax = plt.subplots()
    ax.plot(freq[:int(num/2)], amp[:int(num/2)])
    ax.set_xlabel("Frequency [Hz]")
    ax.set_ylabel("Amplitude")
    ax.grid()
    plt.show()
   
    