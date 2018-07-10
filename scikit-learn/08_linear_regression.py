# http://scikit-learn.org/stable/modules/linear_model.html#ordinary-least-squares

from sklearn import linear_model

# LinearRegression takes in its fit method arrays X, y and stores the coefficients w of the linear model in its
# coef_ member.
reg = linear_model.LinearRegression()

reg.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])

print(reg.coef_)  # [0.5 0.5]
