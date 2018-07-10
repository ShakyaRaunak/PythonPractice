# https://www.tutorialspoint.com/scipy/scipy_fftpack.htm

"""
Fourier Transformation is computed on a time domain signal to check its behavior in the frequency domain.
"""

import numpy as np
# Importing the fft, inverse fft, dct, inverse dct functions from fftpackage
from scipy import fftpack
from scipy.fftpack import dct
from scipy.fftpack import fft
from scipy.fftpack import idct
from scipy.fftpack import ifft

# create an array with random n numbers
x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])

# Applying the fft function
y = fft(x)
print(y)
print()

yinv = ifft(y)
print(yinv)
print()

# Creating a signal with a time step of 0.02 seconds
time_step = 0.02
period = 5.
time_vec = np.arange(0, 20, time_step)
sig = np.sin(2 * np.pi / period * time_vec) + 0.5 * np.random.randn(time_vec.size)
print(sig.size)
print()

# scipy.fftpack.fftfreq() will generate the sampling frequencies and scipy.fftpack.fft() will compute the fast Fourier transform.
sample_freq = fftpack.fftfreq(sig.size, d=time_step)
sig_fft = fftpack.fft(sig)
print(sig_fft)
print()

"""
A Discrete Cosine Transform (DCT) expresses a finite sequence of data points in terms of a sum of cosine functions 
oscillating at different frequencies.
"""
print(dct(np.array([4., 3., 5., 10., 5., 3.])))
print()

"""
The inverse discrete cosine transform reconstructs a sequence from its discrete cosine transform (DCT) coefficients.
"""
print(idct(np.array([4., 3., 5., 10., 5., 3.])))
