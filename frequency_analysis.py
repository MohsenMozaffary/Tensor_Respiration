from scipy.signal import butter, freqz, lfilter
import numpy as np


# Bandpass filtering signal in desired frequency range
def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

#  Finding the peak frequency difference between estimated signal and ground truth in beats per minute
def peak_frequency_difference(signal1, signal2, fs):
    # Compute the FFT of the signals
    fft_signal1 = np.fft.fft(signal1)
    fft_signal2 = np.fft.fft(signal2)

    # Calculate the frequencies corresponding to each FFT bin
    freqs = np.fft.fftfreq(len(signal1), 1 / fs)

    # Find the frequency index with the maximum amplitude for each signal
    max_freq_index_signal1 = np.argmax(np.abs(fft_signal1))
    max_freq_index_signal2 = np.argmax(np.abs(fft_signal2))

    # Calculate the frequencies at which each signal has maximum amplitude
    max_freq_signal1 = np.abs(freqs[max_freq_index_signal1])
    max_freq_signal2 = np.abs(freqs[max_freq_index_signal2])

    # Calculate the difference between the frequencies
    peak_frequency_diff = np.abs(60*max_freq_signal1 - 60*max_freq_signal2)

    return peak_frequency_diff

def normalized_bandpower(signal, fs, freq_range):
    # Compute the power spectrum using the Fourier transform
    spectrum = np.fft.fft(signal)
    freqs = np.fft.fftfreq(len(signal), 1 / fs)
    
    # Calculate the total power of the signal
    total_power = np.sum(np.abs(spectrum) ** 2)
    
    # Determine the indices corresponding to the desired frequency range
    freq_indices = np.where((freqs >= freq_range[0]) & (freqs <= freq_range[1]))[0]
    
    # Compute the power within the specified frequency range
    bandpower = np.sum(np.abs(spectrum[freq_indices]) ** 2)
    
    # Normalize the bandpower
    normalized_bandpower = bandpower / total_power
    
    return normalized_bandpower