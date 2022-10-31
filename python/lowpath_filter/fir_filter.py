import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def constructFIR(numtaps, cutoff, freq):
    b = signal.firwin(numtaps=numtaps, cutoff=cutoff, fs=freq, window='hanning')
    return b

def applyFIR(x, numtaps, cutoff, freq):
    b = constructFIR(numtaps, cutoff, freq)
    y = signal.lfilter(b, 1, x)
    print(b)
    return y

def applyRawFIR(x, numtaps, cutoff, freq):
    b = constructFIR(numtaps, cutoff, freq)
    
    y = np.zeros_like(x)    
    for i in range(y.shape[0]):
        for j in range(len(b)):
            if (i-j) >= 0:
                y[i] += b[j]*x[i-j]
    return y


if __name__ == "__main__":
    pass