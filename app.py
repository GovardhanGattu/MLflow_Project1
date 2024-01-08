from flask import Flask,request,render_template
import pandas as pd
from src.exception import CustomeException
from src.logger import logging
from src.pipeline.predict_pipeline import PredictPipeline,CustomData

application =Flask(__name__,static_folder='/static')
app=application

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=["GET","POST"])
def predit_data():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(
            age=request.form.get('age'),
            bmi=request.form.get('bmi'),
            sex=request.form.get('sex'),
            children=request.form.get('children'),
            smoker=request.form.get('smoker'),
            region=request.form.get('region')
        )

        dataframe=data.prepare_data_frame()
        predict_userdata=PredictPipeline()
        result=predict_userdata.predict_pipeline(dataframe)

        return render_template('home.html',result=result[0])
    

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)      