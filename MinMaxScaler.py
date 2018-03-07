class MinMaxScaler():
    def __init__(self, feature_range=(0, 1), copy=True):
        from sklearn.preprocessing import MinMaxScaler
        self.feature_range = feature_range
        self.copy = copy
        self.estimator = MinMaxScaler()

    def fit(self, X, y=None):
        return self.estimator.fit(X, y)

    def transform(self, X):
        return self.estimator.transform(X)

#Testing Code
data = [[-1, 2], [-0.5, 6], [0, 10], [1, 18]]
scaler = MinMaxScaler()
print(scaler.fit(data))
print(scaler.transform(data))
print(scaler.transform([[2, 2]]))