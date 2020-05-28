from flask import Flask, render_template, request
from clean import data_final, dftop25, data_bir
from prediction import prediction
from prediction2 import prediction2
from plots import trend, sugarscale, gravity, ibu, color
# from plots import figuretop, brewmethod

app=Flask(__name__)

@app.route('/')
def home():
    return render_template ('home.html')

@app.route('/data')
def data():
    data = data_bir()
    return render_template ('data.html', data=data)

@app.route('/plots')
def plots():
    data = data_bir()
    return render_template('plots.html', data=data)

@app.route('/prediction',methods= ['GET','POST'])
def prediction_html():
    if request.method == 'POST':
        data = request.form
        data=data.to_dict()
        data['Color']=float(data['Color'])
        data['ABV']=float(data['ABV'])
        hasil=prediction(data)
        return render_template('result.html', hasil_prediksi=hasil)
    return render_template('prediction.html')

@app.route('/prediction2',methods= ['GET','POST'])
def prediction2_html():
    if request.method == 'POST':
        data = request.form
        data=data.to_dict()
        data['OG']=float(data['OG'])
        data['FG']=float(data['FG'])
        data['Size(L)']=float(data['Size(L)'])
        data['BoilSize']=float(data['BoilSize'])
        hasil=prediction2(data)
        return render_template('result2.html', hasil_prediksi2=hasil)
    return render_template('prediction2.html')



if __name__ == '__main__':
    app.run(debug=True,port=2000)