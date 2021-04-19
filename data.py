import pandas as pd
 
class Data:
    
    def __init__(self, path):
        self.data = pd.read_csv(path, sep=',')
        self.col = {i: column for i, column in enumerate(self.data.columns)}
        self.cat = [7, 9, 10, 17, 18] # categorical columns, except for the Cloud9am and Cloud3pm columns
        self.num = [2, 3, 4, 5, 6, 8, 11, 12, 13, 14, 15, 16, 19, 20] # numerical columns
        self.map = {'No': 0, 'Yes': 1}
        print(self.col)

    def drop_rows(self, column_no):
        self.data = self.data[self.data[self.col[column_no]].notna()]

    def drop_column(self, column_no):
        self.data = self.data.drop(self.col[column_no], axis=1)

    def fill_na_values(self, column_no, type):
        """
        we replace the missing data in the categorical columns with the most frequent value and
        the missing data in the numerical columns with the most frequent mean of all of the values
        """
        if type == "cat":
            value = self.data[self.col[column_no]].value_counts().argmax()
            self.data[self.col[column_no]].fillna(value, inplace=True)
        elif type == "num":
            value = self.data[self.col[column_no]].mean()
            self.data[self.col[column_no]].fillna(value, inplace=True) if column_no != 6 else self.data[self.col[column_no]].fillna(int(value), inplace=True)

    def update_rain_today(self):
        
        new_rain_col = []
        
        for x, y in zip(self.data[self.col[4]], self.data[self.col[21]]):
            if x != 'nan' and y == 'nan':
                if x > 1.0:
                    new_rain_col.append('Yes')
                else:
                    new_rain_col.append('No')
            else:
                new_rain_col.append(y)

        self.data[self.col[21]] = new_rain_col
    
    def map_binary(self, column_no):
        # map No to 0 and Yes to 1
        new_col = []
        for x in self.data[self.col[column_no]]:
            new_col.append(self.map[x])
        self.data[self.col[column_no]] = new_col

    def preprocess(self):
        
        self.data.drop_duplicates(inplace=True) # drop all the duplicates
        self.drop_rows(22) # drop all the rows that have a null value for the RainTomorrow column 
        self.update_rain_today() # replace the NA values of the RainToday column with the right value
        self.drop_rows(21) # drop all the rows that have a null value for the RainTomorrow column 
        
        for col in [21, 22]:
            self.map_binary(col) 

        for col in self.cat:
            self.fill_na_values(col, "cat")
        for col in self.num:
            self.fill_na_values(col, "num")
        

    