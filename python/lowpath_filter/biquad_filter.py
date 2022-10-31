import numpy as np

BUFFER_SIZE = 10
class biquadFilter:
    def __init__(self, fc, fs) -> None:
        self.fc = fc # cutoff frequency
        self.fs = fs # sampling frequency
        self.q = 1./np.sqrt(2)
        self.calCoefs()
        
    def apply(self, input_signals):
        input_buffer = np.zeros(2)
        output_buffer = np.zeros(2)
        results = np.zeros_like(input_signals)        
        
        for i in range(input_signals.size):
            input = input_signals[i]
            if i == 0:
                output = input
            elif i == 1:
                output = input
            else:
                output = self.coefs[0]*input + self.coefs[1]*input_buffer[0] + self.coefs[2]*input_buffer[1] - self.coefs[3]*output_buffer[0] - self.coefs[4]*output_buffer[1] 
        
            input_buffer[1] = input_buffer[0]
            input_buffer[0] = input
            
            output_buffer[1] = output_buffer[0]
            output_buffer[0] = output
            
            results[i] = output
            
        return results
        
    
    def calCoefs(self):
        self.coefs = np.zeros(5)
        
        omega = 2.0*np.pi*self.fc/self.fs
        cos_omega = np.cos(omega)
        sin_omega = np.sin(omega)
        
        alpha_q = sin_omega / (2.0*self.q)
        
        a0 = 1.0 + alpha_q
        self.coefs[0] = ((1.0 - cos_omega)/2.0) / a0
        self.coefs[1] = (1.0 - cos_omega) / a0
        self.coefs[2] = ((1.0 - cos_omega)/2.0) / a0
        self.coefs[3] = (-2.0 * cos_omega) / a0
        self.coefs[4] = (1.0 - alpha_q) / a0