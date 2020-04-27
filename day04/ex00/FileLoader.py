import pandas as pd

class FileLoader:

    @staticmethod
    def load(path):
        df = pd.read_csv(path)
        print('Dimensions of dataframe : {}/{}'.\
        format(df.shape[0], df.shape[1]))
        return df
    
    @staticmethod
    def display(df, n):
        if n < 0:
            print(df.tail(n * -1))
        if n >= 0:
            print(df.head(n))
