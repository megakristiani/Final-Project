import pickle
from pandas import DataFrame

model = pickle.load(open("bpom.sav",'rb'))

def prediction(data):
    df= DataFrame(data,index=[0])
    hasil = model.predict(df)
    hasil_prediksi=[]
    if hasil ==1:
        hasil_prediksi.append('Ya')
    elif hasil ==2:
        hasil_prediksi.append('Ya')
    if hasil ==5:
        hasil_prediksi.append('Ya')
    else:
        hasil_prediksi.append('Tidak')
    return hasil_prediksi[0]