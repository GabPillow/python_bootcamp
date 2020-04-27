import pandas as pd

def howManyMedals(data, name):
    data.set_index("Name", inplace=True)
    data = data.loc[name]
    medalbook = {}
    for index, row in data.iterrows():
        if not row["Year"] in medalbook:
            medalbook[row["Year"]] = {'G' : 0, 'S' : 0, 'B': 0}
        if row["Medal"] == 'Gold':
            medalbook[row["Year"]]['G'] += 1
        elif row["Medal"] == 'Silver':
            medalbook[row["Year"]]['S'] += 1
        elif row["Medal"] == 'Bronze':
            medalbook[row["Year"]]['B'] += 1

    return medalbook

