import pandas as pd

def data_bir():
    df = pd.read_csv('display.csv', encoding='latin1')
    return df

def dftop25():
    df = pd.read_csv('recipeData.csv', encoding='latin1')
    top25=df['Style'].value_counts(ascending=False)[0:26]
    dftop25=pd.DataFrame({
        'Style':top25.index,
        'Sum':top25.values
    }, index=range(26))
    return dftop25

def data_final():
    dffinal = pd.read_csv('datafinal.csv')
    return dffinal

