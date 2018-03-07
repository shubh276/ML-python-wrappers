class DataCleaning():
    def __init__(self):
        pass

    def replace_outliers(self, X, m=2):
        import numpy as np
        self.X = np.array(X)
        n_col = self.X.shape[1]
        for i in range(n_col):
            temp_col = self.X[:, i]
            temp_col[abs(temp_col - np.mean(temp_col)) > m * np.std(temp_col)] = np.mean(temp_col)
            self.X[:, i] = temp_col
        return self.X

    def remove_duplicates(self,X):
        import numpy as np
        import pandas as pd
        self.X = X
        df = pd.DataFrame(self.X)
        return np.array(df.drop_duplicates())


# Testing code
#Replace outliers
data1 = [[2, 4, 3], [5, 10, 8], [100, 4, 9], [4, 6, 2],[4, 6, 2], [5, 7, 1], [4, 3, 1], [7, 1, 6]]
print(DataCleaning().replace_outliers(data1))

#Remove duplicates
print(DataCleaning().remove_duplicates(data1))