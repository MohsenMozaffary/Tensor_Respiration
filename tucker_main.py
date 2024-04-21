"""
Respiration rate estimation using thermal camera through tucker decomposition
Copyright (c) [2024] [Mohsen Mozafari Ghadikolaei]

Licensed under the MIT License (https://opensource.org/licenses/MIT)
"""

"""
Title: [Respiration Rate Estimation from Thermal Video of Masked and Unmasked Individuals Using Tensor Decomposition]
Authors: [Mohsen Mozafari, AJ Law, JR Green, RA Goubran]
Publication: [2022 IEEE International Instrumentation and Measurement Technology Conference (I2MTC)]
Year: [2022]
"""


from tensorly.decomposition import tucker
from frequency_analysis import *

# Finding the source which has more respiratory information.
def select_source(signal1, signal2, freq_range, fs):
    normalized1 = normalized_bandpower(signal1, fs, freq_range)
    normalized2 = normalized_bandpower(signal2, fs, freq_range)
    if normalized1> normalized2:
        return 0
    else:
        return 1
# Find the tucker decomposition factors.
def run_tucker(data, rank=[2, 2, 2]):
    core, factors = tucker(data, rank)
    return core, factors
# Select the respiratory source.
def find_source(factors, freq_range, fs, lowcut = 0.05, highcut = 0.7, order = 4):
    selected_source = select_source(factors[0][:,0], factors[0][:,1], freq_range, fs)
    output = butter_bandpass_filter(factors[0][:,selected_source], lowcut, highcut, fs, order)
    return output