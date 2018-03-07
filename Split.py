class Split():
    def __init__(self):
        pass

    def train_test_split(self, *arrays, **options):
        from sklearn.model_selection import train_test_split
        self.input_array = arrays
        self.input_options = options
        return train_test_split(*self.input_array, **self.input_options)

    def select_column(self,X,cols):
        import numpy as np
        self.X = np.array(X)
        self.cols = cols
        n_rows = self.X.shape[0]
        n_cols = len(self.cols)
        temp = np.random.rand(n_rows, n_cols)
        for i in range(n_cols):
            temp[:,i] = self.X[:,self.cols[i]]
        return temp

    def date_split(self,X,split_date):
        import pandas as pd
        self.X = pd.DataFrame(X)
        self.split_date = pd.to_datetime(split_date)
        self.X[0] = pd.to_datetime(self.X[0])
        df_training = self.X.loc[self.X[0] <= split_date]
        df_test = self.X.loc[self.X[0] > split_date]
        return df_training, df_test

#Testing Code
#train-test-spli-percentage
import numpy as nump
X, y = nump.arange(10).reshape((5, 2)), range(5)
X_train, X_test, y_train, y_test = Split().train_test_split(X, y, test_size=0.33, random_state=42)
print(X_train)
print(y_train)
print(X_test)
print(y_test)

#select-column
data1 = [[2, 4, 3], [5, 10, 8], [100, 4, 9], [4, 6, 2],[4, 6, 2], [5, 7, 1], [4, 3, 1], [7, 1, 6]]
print(Split().select_column(data1,[0,2]))

#date-spliting
data2 = [['01/10/2015', 21, 31],['01/11/2015', 22, 32],['01/12/2015', 23, 33],['01/1/2016', 24, 34]]
a1, a2 = Split().date_split(data2,'01/11/2015')
print(a1)
print(a2)

#date-time-splitting
data3 = [['01/10/2015 02:04:52', 21, 31],['01/10/2015 02:10:51', 22, 32],['01/10/2015 02:01:59', 23, 33],['01/10/2015 02:07:52', 24, 34]]
a1, a2 = Split().date_split(data3,'01/10/2015 02:05:01')
print(a1)
print(a2)