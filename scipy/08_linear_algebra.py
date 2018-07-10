# https://www.tutorialspoint.com/scipy/scipy_linalg.htm

import numpy as np
from scipy import linalg

# Declaring the numpy arrays
a = np.array([[3, 2, 0], [1, -1, 0], [0, 5, 1]])
b = np.array([2, 4, -1])

"""
The scipy.linalg.solve feature solves the linear equation a * x + b * y + c * z = d, for the unknown x, y, z values.
"""
x = linalg.solve(a, b)
print(x)  # [ 2. -2.  9.]
print()

# Finding a Determinant using the det() function. It takes a matrix as input and returns a scalar value.
A = np.array([[1, 2], [3, 4]])
x = linalg.det(A)
print(x)  # -2.0
print()

# Eigenvalues and Eigenvectors
"""
The eigenvalue-eigenvector problem is one of the most commonly employed linear algebra operations.
We can find the Eigen values (λ) and the corresponding Eigen vectors (v) of a square matrix (A) by considering the following relation −
Av = λv

The scipy.linalg.eig computes the eigenvalues from an ordinary or generalized eigenvalue problem and returns the Eigen values and 
the Eigen vectors.
"""
A = np.array([[1, 2], [3, 4]])
l, v = linalg.eig(A)
print(l)  # printing the result for eigen values
print(v)  # printing the result for eigen vectors
print()

# Singular Value Decomposition
"""
A Singular Value Decomposition (SVD) can be thought of as an extension of the eigenvalue problem to matrices that are not square.

The scipy.linalg.svd factorizes the matrix ‘a’ into two unitary matrices ‘U’ and ‘Vh’ and a 1-D array ‘s’ of singular values 
(real, non-negative) such that a == U*S*Vh, where ‘S’ is a suitably shaped matrix of zeros with the main diagonal ‘s’.
"""
a = np.random.randn(3, 2) + 1.j * np.random.randn(3, 2)
U, s, Vh = linalg.svd(a)
print(U, Vh, s)
