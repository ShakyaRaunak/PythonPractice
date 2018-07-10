# https://www.scipy-lectures.org/packages/scikit-image/index.html

from skimage import data
from skimage import filters

camera = data.camera()
print('camera.dtype: %s' % camera.dtype)

print('camera.shape:', end=' ')
print(camera.shape)

filtered_camera = filters.gaussian(camera, 1)
print('type(filtered_camera): %s' % type(filtered_camera))
