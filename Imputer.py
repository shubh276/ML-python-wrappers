class Imputer():
    def __init__(self, missing_values='NaN', strategy='mean', axis=0, verbose=0, copy=True):
        from sklearn.preprocessing import Imputer
        self.missing_values = missing_values
        self.strategy = strategy
        self.axis = axis
        self.verbose = verbose
        self.copy = copy
        self.estimator = Imputer()

    def fit(self, X, y=None):
        return self.estimator.fit(X)

    def transform(self, X):
        return self.estimator.transform(X)

#Testing Code
import numpy as np
imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
imp.fit([[1, 2], [np.nan, 3], [7, 6]])
X = [[np.nan, 2], [6, np.nan], [7, 6]]
print(imp.transform(X))