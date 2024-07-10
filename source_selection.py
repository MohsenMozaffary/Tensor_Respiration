import numpy as np

"""
This code is used to select the respiratory source
between the extracted signals from Canonical Polyadic Decomposition
It is assuming that the low and high frequency in respiratory source 
are 0.1 and 0.7 Hz respectively.
The returned signal from select_resp_signal function is the selected signal
"""

def get_frequency_info(signal, sampling_freq, low_freq, high_freq):
        n = len(signal)
        freqs = np.fft.fftfreq(n, d=1/sampling_freq)
        fft_values = np.fft.fft(signal)
        
        idx = np.where((freqs >= low_freq) & (freqs <= high_freq))[0]
        
        freq_info = np.sum(np.abs(fft_values[idx]))
        
        return freq_info

def select_resp_signal(signals, sampling_freq):
    
    low_freq = 0.1
    high_freq = 0.7
    max_info = -np.inf
    best_signal = None
    
    for signal in signals:
        freq_info = get_frequency_info(signal, sampling_freq, low_freq, high_freq)
        if freq_info > max_info:
            max_info = freq_info
            best_signal = signal
    
    return best_signal