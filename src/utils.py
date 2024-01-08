import sys
import os
import pickle
from src.exception import CustomeException
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

def saveobject(filepath,object):
    
    try:
        dir_path = os.path.dirname(filepath)

        os.makedirs(dir_path, exist_ok=True)

        with open(filepath, "wb") as file_obj:
            pickle.dump(object, file_obj)

    except Exception as e:
        raise CustomeException(e,sys)
    

def evaluatemodel(X_train,Y_train,X_test,Y_test,models,params):
    report= {}
    try:
        for i in range(len(list(models))):
            model=list(models.values())[i]
            parameters=params[list(models.keys())[i]]
            grid_search=GridSearchCV(model,parameters,cv=3)
            grid_search.fit(X_train,Y_train)

            model.set_params(**grid_search.best_params_)
            model.fit(X_train,Y_train)
            train_predict=model.predict(X_train)
            test_predict=model.predict(X_test)

            train_model_score=r2_score(Y_train,train_predict)
            test_model_score=r2_score(Y_test,test_predict)
            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise CustomeException(e,sys)
    

def loadobject(filepath):
    try:
        with open(filepath,'rb') as fileobject:
            return pickle.load(fileobject)
        
    except Exception as e:
        raise CustomeException(e,sys)
