class Aggregation():
    def __init__(self):
        pass

    def max(self,X):
        import numpy as np
        self.X = np.array(X)
        return self.X.max(axis=0)

    def min(self,X):
        import numpy as np
        self.X = np.array(X)
        return self.X.min(axis=0)

    def mean(self,X):
        import numpy as np
        self.X = np.array(X)
        return self.X.mean(0)

    def sum(self,X):
        import numpy as np
        self.X = np.array(X)
        return self.X.sum(axis=0)

    def std(self,X):
        import numpy as np
        self.X = np.array(X)
        return self.X.std(0)




# Testing Code
# max
data = [[  1,   1,   2], [ 99,   2,   3], [360,  10,  11]]
print(Aggregation().max(data))

# min
print(Aggregation().min(data))

#mean
data = [2,4,5,1,6,5,40]
print(Aggregation().mean(data))

#sum
print(Aggregation().sum(data))

#std
print(Aggregation().std(data))