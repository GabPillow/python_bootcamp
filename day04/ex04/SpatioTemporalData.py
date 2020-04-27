import pandas as pd

class SpatioTemporalData:
    def __init__(self, data):
        self.data = data

    def when(self, location):
        return self.data.drop_duplicates(subset = ["Year"])\
        .set_index("City").loc[location, "Year"].values.tolist()
    
    def where(self, date):
        return self.data.set_index("Year").loc[date, "City"].iloc[0]