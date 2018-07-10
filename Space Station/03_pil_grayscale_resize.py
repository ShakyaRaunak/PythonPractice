# https://www.sitepoint.com/manipulating-images-with-the-python-imaging-library/
from PIL import Image

# Example 1 :
# Convert to a grayscale image, the L parameter was used with convert()
img = Image.open('map.jpg').convert('L')
img.show()
img.save('map-grayscale.png', 'png')

# Example 2 :
# Resize an image
img = Image.open('map.jpg').convert('L')
new_img = img.resize((256, 256))
new_img.save('map-256x256.png', 'png')
