# http://scikit-learn.org/stable/modules/linear_model.html#ridge-regression

from sklearn import linear_model

# As with other linear models, Ridge will take in its fit method arrays X, y and will store the coefficients w of the
# linear model in its coef_ member:
reg = linear_model.Ridge(alpha=.5)

reg.fit([[0, 0], [0, 0], [1, 1]], [0, .1, 1])
# Ridge(alpha=0.5, copy_X=True, fit_intercept=True, max_iter=None, normalize=False, random_state=None, solver='auto', tol=0.001)

print(reg.coef_)  # [0.34545455 0.34545455]
print(reg.intercept_)  # 0.13636363636363638
