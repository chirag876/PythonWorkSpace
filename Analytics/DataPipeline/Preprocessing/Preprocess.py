import pandas as pd

class Preprocess:

    def __init__(self,data) -> None:
        self.data=data

    def drop_null(self):
        self.data = self.data.dropna()

    def drop_duplicates(self):
        self.data = self.data.drop_duplicates()

    def fill_missing_values(self):
        for col in self.data.columns:
            if self.data[col].dtype == 'object':
                self.data[col].fillna(self.data[col].mode()[0], inplace=True)
            else:
                self.data[col].fillna(self.data[col].median(), inplace=True)
 
    def Preprocessed(self):
        #self.drop_null()
        #self.drop_duplicates()
        #self.fill_missing_values()
        return self.data