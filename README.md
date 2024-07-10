# Respiratory Signal Estimation from Thermal Video using Tensor Decomposition

This repository contains the codes for estimating respiratory signals through thermal video data using tensor decomposition methods such as Canonical Polyadic Decomposition (CPD) and Tucker Decomposition.

## Overview

Tensor decomposition methods are powerful tools for extracting signals from multi-dimensional data. In this project, we utilize:
- **Canonical Polyadic Decomposition (CPD)**
- **Tucker Decomposition**

to extract respiratory signals from thermal video data. These methods help isolate the desired signal from noise and other interferences.

## Files

- **`tucker_main.py`**: Contains the code to extract and filter the respiratory signals using the Tucker decomposition method.

## Dependencies

Ensure you have the following libraries installed:

- `scipy`
- `numpy`
- `tensorly==0.7.0`

You can install the dependencies using the following command:

```bash
pip install scipy numpy tensorly==0.7.0
