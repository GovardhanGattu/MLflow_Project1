import os
import sys
from src.exception import CustomeException
from src.logger import logging
from dataclasses import dataclass
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from xgboost import XGBRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from catboost import CatBoostRegressor
from sklearn.ensemble import (
    RandomForestRegressor,
    AdaBoostRegressor,
    GradientBoostingRegressor
    )
from src.utils import saveobject,evaluatemodel

@dataclass
class ModelTrainerConfig():
    model_path=os.path.join('artifacts','model.pkl')

class ModelTrainer():
    def __init__(self):
        self.modeltrainerconfig=ModelTrainerConfig()

    def initiate_model_training(self,train_data,test_data):
        try:
            X_train,Y_train,X_test,Y_test =(
                train_data[:,:-1],
                train_data[:,-1],
                test_data[:,:-1],
                test_data[:,-1]
                )
            
            models ={
                "RandomForestRegressor":RandomForestRegressor(),
                "DecisionTree":DecisionTreeRegressor(),
                "LinearRegression":LinearRegression(),
                "catboost":CatBoostRegressor(),
                "Kneighbour":KNeighborsRegressor(),
                "XGRegressor":XGBRegressor(),
                "Adaboosting":AdaBoostRegressor(),
                "GradientBoostingRegressor":GradientBoostingRegressor()   
        }   

            params={
                "DecisionTree": {
                    'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson']
                },
                "RandomForestRegressor":{
                    'n_estimators': [8,16,32,64,128,256]
                },
                "GradientBoostingRegressor":{
                    'learning_rate':[.1,.01,.05,.001],
                    'subsample':[0.6,0.7,0.75,0.8,0.85,0.9],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "LinearRegression":{},
                "XGRegressor":{
                    'learning_rate':[.1,.01,.05,.001],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "catboost":{
                    'depth': [6,8,10],
                    'learning_rate': [0.01, 0.05, 0.1],
                    'iterations': [30, 50, 100]
                },
                "Adaboosting":{
                    'learning_rate':[.1,.01,0.5,.001],
                    'n_estimators': [8,16,32,64,128,256]

                    
                },
                "Kneighbour":{}

                
            }
            
            model_report :dict=evaluatemodel(
                X_train=X_train,Y_train=Y_train,X_test=X_test,Y_test=Y_test,models=models,params=params)

            best_model_score=max(sorted(model_report.values()))
            best_model_name=list(model_report.keys())[list(model_report.values()).index(best_model_score)]
            best_model=models[best_model_name]
            print(f"Best Model {best_model} with R2 score of{best_model_score}")

            saveobject(
                filepath=self.modeltrainerconfig.model_path,object=best_model
            )

            
        except Exception as e:
            raise CustomeException(e,sys)