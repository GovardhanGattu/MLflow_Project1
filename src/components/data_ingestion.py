import sys
import os
import pandas as pd
from src.exception import CustomeException
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
from src.components.data_transformation import DataTransformation,DataTrasformationConfig
from src.components.model_trainer import ModelTrainer,ModelTrainerConfig

@dataclass
class DataIngestionConfig():
    train_data_path=os.path.join('artifacts','traindata.csv')
    test_data_path=os.path.join('artifacts','testdata.csv')
    actual_data_path=os.path.join('artifacts','insurancedata.csv')

class DataIngestion():
    def __init__(self):
        self.dataingestionconfig=DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            os.makedirs(os.path.dirname(self.dataingestionconfig.train_data_path),exist_ok=True)
            df=pd.read_csv("Notebook/data/insurance.csv")
            df.to_csv(self.dataingestionconfig.actual_data_path,index=False,header=True)
            
            train_dataset,test_dataset= train_test_split(df,train_size=0.2,random_state=25)
            train_dataset.to_csv(self.dataingestionconfig.train_data_path,index=False,header=True)
            test_dataset.to_csv(self.dataingestionconfig.test_data_path,index=False,header=True)

            return(
                self.dataingestionconfig.train_data_path,
                self.dataingestionconfig.test_data_path
            )

        except Exception as e:
            raise CustomeException(e,sys)
        
if __name__=="__main__":
    dataobj=DataIngestion()
    train_dataset_path,test_dataset_path=dataobj.initiate_data_ingestion()

    datatransformation=DataTransformation()
    train_arr,test_arr,_=datatransformation.initialize_data_transformation(train_dataset_path,test_dataset_path)
    
    model =ModelTrainer()
    model.initiate_model_training(train_arr,test_arr)

