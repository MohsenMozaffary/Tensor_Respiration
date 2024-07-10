import cv2
import numpy as np
from tensorly.decomposition import parafac
from source_selection import select_resp_signal
""""
This code is used to extract respiratory signal from thermal video data using Canonical Polyadic Decompostion (CPD).
The input data will be a 3-D numpy array with dimensions of (Time x Width x Height)
n_sources is the expected number of sources in the video
fps is the frame per second for the input data 
The first output is the selected respiratory source and the second output is all
sources that are extracted from CPD.
"""
def Extract_respiration(input_data, n_sources = 2, fps = 30):
    extracted_signals = np.zeros((n_sources, input_data.shape[0]))
    factors = parafac(input_data, rank=n_sources)
    for n in range(n_sources):
        sig = factors[1][0][:,n]
        sig = (sig - np.min(sig))/(np.max(sig) - np.min(sig))
        extracted_signals[n] = sig

    respiratory_source = select_resp_signal(extracted_signals, fps)
    return respiratory_source, factors[1][0]