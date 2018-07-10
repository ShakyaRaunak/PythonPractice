# http://scikit-learn.org/stable/modules/linear_model.html#lasso

"""
The Lasso is a linear model that estimates sparse coefficients. It is useful in some contexts due to its tendency to
prefer solutions with fewer parameter values, effectively reducing the number of variables upon which the given solution
is dependent.
"""
from sklearn import linear_model

# The implementation in the class Lasso uses coordinate descent as the algorithm to fit the coefficients.
reg = linear_model.Lasso(alpha=0.1)

reg.fit([[0, 0], [1, 1]], [0, 1])
# Lasso(alpha=0.1, copy_X=True, fit_intercept=True, max_iter=1000, normalize=False, positive=False, precompute=False, random_state=None, selection='cyclic', tol=0.0001, warm_start=False)

print(reg.predict([[1, 1]]))  # [0.8]
