# https://www.datacamp.com/community/tutorials/machine-learning-python

import matplotlib.pyplot as plt
from sklearn import datasets

# Load in the `digits` data
digits = datasets.load_digits()

# Join the images and target labels in a list
images_and_labels = list(zip(digits.images, digits.target))  # Zips two numpy arrays together and save into a variable

# for every element in the list
for index, (image, label) in enumerate(images_and_labels[:8]):
    # initialize a subplot of 2X4 at the i+1-th position
    plt.subplot(2, 4, index + 1)

    # Don't plot any axes
    plt.axis('off')

    # Display images in all subplots
    plt.imshow(image, cmap='Greys', interpolation='nearest')  # in place of : cmap=plt.cm.gray_r

    # Add a title to each subplot
    plt.title('Training: ' + str(label))

# Show the plot
plt.show()
