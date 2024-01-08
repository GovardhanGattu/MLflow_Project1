import sys
import os
import pandas as pd
from src.exception import CustomeException
from src.logger import logging
from src.utils import loadobject

class PredictPipeline():
    def __init__(self):
        pass

    def predict_pipeline(self,inputdata):
        try:
            model_path=os.path.join('artifacts','model.pkl')
            model=loadobject(filepath=model_path)
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            preprocessor=loadobject(filepath=preprocessor_path)
            scaled_data=preprocessor.transform(inputdata)
            model_prediction=model.predict(scaled_data)
            
            return model_prediction
        
            
        except Exception as e:
            raise CustomeException(e,sys)

class CustomData():
    def __init__(self,
                 age: int,
                 bmi:float,
                 sex:str,
                 children:int,
                 smoker:str,
                 region:str,
                 ):
        
        self.age=age
        self.bmi=bmi
        self.sex=sex
        self.children=children
        self.smoker=smoker
        self.region=region
        

    def prepare_data_frame(self):
        try:
            custom_data={
                'age':[self.age],
                'bmi':[self.bmi],
                'sex':[self.sex],
                'children':[self.children],
                'smoker': [self.smoker],
                'region':[self.region],
            }

            custom_dataframe=pd.DataFrame(custom_data)

            return custom_dataframe
        
        except Exception as e:
            raise CustomeException(e,sys)