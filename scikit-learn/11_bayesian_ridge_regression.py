# http://scikit-learn.org/stable/modules/linear_model.html#bayesian-ridge-regression

from sklearn import linear_model

# Bayesian Ridge Regression is used for regression:
X = [[0., 0.], [1., 1.], [2., 2.], [3., 3.]]
Y = [0., 1., 2., 3.]

reg = linear_model.BayesianRidge()

reg.fit(X, Y)
# BayesianRidge(alpha_1=1e-06, alpha_2=1e-06, compute_score=False, copy_X=True, fit_intercept=True, lambda_1=1e-06, lambda_2=1e-06, n_iter=300, normalize=False, tol=0.001, verbose=False)

# After being fitted, the model can then be used to predict new values:
print(reg.predict([[1, 0.]]))  # [0.50000013]
print(reg.predict([[1, 0.]]))  # [0.50000013]

# The weights w of the model can be accessed:
print(reg.coef_)  # [0.49999993 0.49999993]
