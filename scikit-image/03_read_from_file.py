# https://www.scipy-lectures.org/packages/scikit-image/index.html

import os

import skimage
from skimage import io

filename = os.path.join(skimage.data_dir, 'camera.png')
print('filename: %s' % filename)

# Reading from files: skimage.io.imread()
camera = io.imread(filename)
