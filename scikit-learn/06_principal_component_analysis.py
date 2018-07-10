# https://www.datacamp.com/community/tutorials/machine-learning-python

"""
High dimensionality of data is a direct result of trying to describe the objects via a collection of features.
Other examples of high dimensional data are, for example, financial data, climate data, neuroimaging, …

The idea in PCA is to find a linear combination of the two variables that contains most of the information.
This new variable or “principal component” can replace the two original variables.
In short, it’s a linear transformation method that yields the directions (principal components) that maximize
the variance of the data.
"""

from sklearn.decomposition import RandomizedPCA, PCA
from sklearn import datasets
import matplotlib.pyplot as plt

# Load in the `digits` data
digits = datasets.load_digits()

# Create a Randomized PCA model that takes two components
randomized_pca = RandomizedPCA(n_components=2)
# You have used the RandomizedPCA() here because it performs better when there’s a high number of dimensions.

# Fit and transform the data to the model
reduced_data_rpca = randomized_pca.fit_transform(digits.data)

# Create a regular PCA model
pca = PCA(n_components=2)

# Fit and transform the data to the model
reduced_data_pca = pca.fit_transform(digits.data)

# Inspect the shape
print(reduced_data_pca.shape)
print('----------------------------------------------------------')

print(reduced_data_rpca)
print('----------------------------------------------------------')

print(reduced_data_pca)
print('----------------------------------------------------------')

# You can now build a scatterplot to visualize the data:
colors = ['black', 'blue', 'purple', 'yellow', 'white', 'red', 'lime', 'cyan', 'orange', 'gray']

for i in range(len(colors)):
    x = reduced_data_rpca[:, 0][digits.target == i]
    y = reduced_data_rpca[:, 1][digits.target == i]

    plt.scatter(x, y, c=colors[i])

plt.legend(digits.target_names, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.title("PCA Scatter Plot")
plt.show()

"""
Note how you explicitly tell the model to only keep two components. This is to make sure that you have two-dimensional 
data to plot. Also, note that you don’t pass the target class with the labels to the PCA transformation because you want 
to investigate if the PCA reveals the distribution of the different labels and if you can clearly separate the instances 
from each other.
"""
