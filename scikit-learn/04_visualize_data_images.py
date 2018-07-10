# https://www.datacamp.com/community/tutorials/machine-learning-python

import matplotlib.pyplot as plt
from sklearn import datasets

# Load in the `digits` data
digits = datasets.load_digits()

# Set up a figure with a figure size of 6 inches wide and 6 inches long. This is your blank canvas where all the
# subplots with the images will appear.
fig = plt.figure(figsize=(6, 6))

# Adjust some parameters: you set the left side of the suplots of the figure to 0, the right side to 1, the bottom to 0
# and the top to 1. The height of the blank space between the suplots is set at 0.005 and the width is set at 0.05.
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)

# For each of the 64 images
for i in range(64):
    # Initialize the subplots: add a subplot in the grid of 8 by 8, at the i+1-th position
    ax = fig.add_subplot(8, 8, i + 1, xticks=[], yticks=[])

    # Display each time one of the images at each position in the grid. As a color map, you take binary colors, which
    # in this case will result in black, gray values and white colors.
    # The interpolation method 'nearest' means that your data is interpolated in such a way that it isn’t smooth.
    ax.imshow(digits.images[i], cmap='Greys', interpolation='nearest')  # in place of : cmap=plt.cm.binary

    # label the image with the target value
    ax.text(0, 7, str(digits.target[i]))

# Show the plot
plt.show()
