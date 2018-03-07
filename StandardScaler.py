class StandardScaler():
    def __init__(self,copy=True, with_mean=True, with_std=True):
        from sklearn.preprocessing import StandardScaler
        self.copy = copy
        self.with_mean = with_mean
        self.with_std = with_std
        self.estimator = StandardScaler()

    def fit(self, X, y=None):
        return self.estimator.fit(X, y)

    def transform(self, X):
        return self.estimator.transform(X)


data = [[0, 0], [0, 0], [1, 1], [1, 1]]
scaler = StandardScaler()
print(scaler.fit(data))
print(scaler.transform(data))
print(scaler.transform([[2, 2]]))