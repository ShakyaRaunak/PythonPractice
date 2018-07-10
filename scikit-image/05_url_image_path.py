# https://www.scipy-lectures.org/packages/scikit-image/index.html

from skimage import io

logo = io.imread('http://scikit-image.org/_static/img/logo.png')
io.imsave('local_logo.png', logo)
