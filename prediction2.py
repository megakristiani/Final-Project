import pickle
from pandas import DataFrame

model = pickle.load(open("bg.sav",'rb'))

def prediction2(data):
    df= DataFrame(data,index=[0])
    hasil_prediksi2 = model.predict(df)
    return hasil_prediksi2[0]