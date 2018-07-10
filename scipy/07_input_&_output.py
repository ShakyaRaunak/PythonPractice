# https://www.tutorialspoint.com/scipy/scipy_input_output.htm

"""
The Scipy.io (Input and Output) package provides a wide range of functions to work around with different format of files.
"""

import numpy as np
import scipy.io as sio

vect = np.arange(10)
# savemat saves a MATLAB file
sio.savemat('array.mat', {'vect': vect})

# loadmat loads a MATLAB file
mat_file_content = sio.loadmat('array.mat')
print(mat_file_content)
print()

# whosmat lists variables inside a MATLAB file i.e. to inspect the contents of a MATLAB file without reading the data into memory.
mat_file_content = sio.whosmat('array.mat')
print(mat_file_content)
