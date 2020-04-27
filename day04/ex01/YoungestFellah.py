import pandas as pd

def youngestFellah(data, year):
    data.set_index("Year", inplace=True)
    data = data.loc[2004]
    data.set_index("Sex", inplace=True)
    datam = data.loc["M", "Age"].values
    dataf = data.loc["F", "Age"].values
    agem = datam[0]
    agef = dataf[0]
    for m,f in zip(datam, dataf):
        if m < agem:
            agem = m
        if f < agef:
            agef = f
    return {'M': agem, 'F': agef}
