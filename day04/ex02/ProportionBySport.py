import pandas as pd

def proportionBySport(data, year, sport, gender):
    data.set_index("Sex", inplace=True)
    data = data.loc[gender]
    data.set_index("Year", inplace=True)
    data = data.loc[year]
    total = data.drop_duplicates(subset = ["Name"]).shape
    data.set_index("Sport", inplace=True)
    onlysport = data.loc[sport].drop_duplicates(subset = "Name").shape
    return onlysport[0] / total[0]
