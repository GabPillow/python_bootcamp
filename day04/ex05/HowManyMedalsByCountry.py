import pandas as pd

def howManyMedalsByCountry(data, country):
    data.set_index("Team", inplace=True)
    data = data.loc[country]
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

