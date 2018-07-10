# Python Imaging Library (PIL)
# convert jpg image to gif
from PIL import Image

Image.open('map.jpg').convert('RGB').save('map.gif')
