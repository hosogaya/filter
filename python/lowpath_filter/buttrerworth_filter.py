import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import pandas as pd

def constructButterworth(lowcut, fs, order =4):
    ''' constrcut butterworth filter 
    '''
    nyq = 0.5 * fs # nyquist frequency
    low = lowcut / nyq # normalize with nyquist frequency
    b, a = signal.butter(order, low, btype='low')
    return b, a # return coefficients


def applyButterworth(x, lowcut, fs, order=4):
    ''' apply butterworth filter
    '''
    b, a = constructButterworth(lowcut, fs, order)
    y = signal.filtfilt(b, a, x)
    print(order, a, b)
    return y

def dummy():
    from fast_fourier_transform import createDummy
    num, fs, x, t = createDummy()
    y = applyButterworth(x, 100, fs, order=4) 
    
    return x, y, t


if __name__=="__main__":
    from fir_filter import applyFIR, applyRawFIR
    from biquad_filter import biquadFilter
    # x, y, t = dummy()
    df = pd.read_csv('sample_data.csv', header=None)
    num = df.shape[0]
    dt = 0.025
    fs = 1./dt
    t = np.arange(0, num*dt, dt)
    x = np.zeros(num)
    x = df[3].values
    
    biqu = biquadFilter(3, fs)
    y = biqu.apply(x)
    # y = applyButterworth(x, 2, fs, order=1)    
    # y = applyFIR(x, 5, 2, fs)

    fig, ax = plt.subplots()
    ax.plot(t, x, label='raw data')
    ax.plot(t, y, label='filtered')
    ax.set_xlabel("Time [s]")
    ax.set_ylabel("Signal")
    ax.grid()
    plt.legend(loc='best')
    plt.show()
    
