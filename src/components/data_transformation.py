import sys
import os
import pandas as pd
import numpy as np
from dataclasses import dataclass
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler 
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from src.exception import CustomeException
from src.utils import saveobject

@dataclass
class DataTrasformationConfig:
    
    preprocessor_obj_filepath=os.path.join('artifacts','Preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.datatransformationconfig=DataTrasformationConfig()

    def get_transformation_object(self):
        try:
            numerical_columns = ['age','bmi','children']
            categorical_columns=['sex','smoker','region']

            numerical_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="median")),
                    ("scaler",StandardScaler(with_mean=False))
                ]
            )

            categorical_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="most_frequent")),
                    ("onehotencoder",OneHotEncoder()),
                    ("scaler",StandardScaler(with_mean=False))
                ]
            )

            preprocessor=ColumnTransformer([
                ('numerical_pipeline',numerical_pipeline,numerical_columns),
                ('categorical_pipeline',categorical_pipeline,categorical_columns)
            ]
            )

            return preprocessor
        
        except Exception as e:
            raise CustomeException(e,sys)
        
    def initialize_data_transformation(self,train_data_path,test_data_path):
        try:
            train_df=pd.read_csv(train_data_path)
            test_df=pd.read_csv(test_data_path)
            target_column="expenses"
            input_features_train_df=train_df.drop(columns=[target_column],axis=1)
            target_feature_train_df=train_df[target_column]
            input_features_test_df=test_df.drop(columns=[target_column],axis=1)
            target_column_test_df=test_df[target_column]
            preprocessor_obj=self.get_transformation_object()
            
            train_df_arr=preprocessor_obj.fit_transform(input_features_train_df)
            test_df_arr=preprocessor_obj.transform(input_features_test_df)

            train_arr=np.c_[train_df_arr,np.array(target_feature_train_df)]
            test_arr=np.c_[test_df_arr,np.array(target_column_test_df)]


            saveobject(
                filepath=self.datatransformationconfig.preprocessor_obj_filepath,
                object=preprocessor_obj

            )
            return(
                train_arr,
                test_arr,
                self.datatransformationconfig.preprocessor_obj_filepath
            )

        except Exception as e:
            raise CustomeException(e,sys)
