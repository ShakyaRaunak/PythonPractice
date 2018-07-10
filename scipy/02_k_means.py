# https://www.tutorialspoint.com/scipy/scipy_cluster.htm

"""
K-means clustering is a method for finding clusters and cluster centers in a set of unlabelled data.
"""

from numpy import vstack, array
from numpy.random import rand
from scipy.cluster.vq import kmeans, vq, whiten

# data generation with three features to explore the clustering
data = vstack((rand(100, 3) + array([.5, .5, .5]), rand(100, 3)))
print(data)
print()

# whitening of data - to rescale each feature dimension of the observation set with whitening.
# Each feature is divided by its standard deviation across all observations to give it unit variance.
data = whiten(data)

# computing K-Means with K = 3 (2 clusters)
centroids, _ = kmeans(data, 3)
# K-Means algorithm adjusts the centroids until sufficient progress cannot be made, i.e. the change in distortion,
# since the last iteration is less than some threshold.
print(centroids)
print()

# assign each sample to a cluster
clx, _ = vq(data, centroids)
# vq function compares each observation vector in the ‘M’ by ‘N’ obs array with the centroids and assigns the observation
# to the closest cluster.

# check clusters of observation
print(clx)
