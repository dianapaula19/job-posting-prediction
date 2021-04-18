import pandas as pd

class Data:
    
    def __init__(self, path):
        self.data = pd.read_csv(path, sep=',')