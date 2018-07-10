# https://www.tutorialspoint.com/python/python_graph_data.htm

"""
One very efficient way to represent graph data is in a sparse matrix: let us call it G. The matrix G is of size N x N,
and G[i, j] gives the value of the connection between node ‘i' and node ‘j’. A sparse graph contains mostly zeros − that is,
most nodes have only a few connections.
"""

import numpy as np

# Example 1
G_dense = np.array([[0, 2, 1],
                    [2, 0, 0],
                    [1, 0, 0]])

G_masked = np.ma.masked_values(G_dense, 0)

from scipy.sparse import csr_matrix

G_sparse = csr_matrix(G_dense)
print(G_sparse.data)  # [2 1 2 1]
print()

# Example 2
G2_data = np.array([
    [np.inf, 2, 0],
    [2, np.inf, np.inf],
    [0, np.inf, np.inf]
])

from scipy.sparse.csgraph import csgraph_from_dense

G2_sparse = csgraph_from_dense(G2_data, null_value=np.inf)
print(G2_sparse.data)  # [2. 0. 2. 0.]
