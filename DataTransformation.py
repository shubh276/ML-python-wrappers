class DataTransformation():
    def __init__(self):
        pass

    def exp(self,X):
        import numpy as np
        x_numpy = np.array(X)
        return np.exp(x_numpy)

    def log(self,X):
        import numpy as np
        x_numpy = np.array(X)
        return np.log(x_numpy)

    def mean(self,X):
        import numpy as np
        self.X = np.array(X)
        return self.X.mean(0)

# Testing Code
# exponential
data = [[  1,   1,   2], [ 3,   2,   3], [3,  4,  5]]
print(DataTransformation().exp(data))

#logarithm
import numpy as np
data2 = [1, np.e, np.e**2, 0]
print(DataTransformation().log(data2))

#Mean
print(DataTransformation().mean(data))