from src.Data_Loader.loader import loader
from src.Feature_Engineering.preprocessing import preprocessor
from src.logger import log
from src.Database.database_builder import database
from src.Modelling.model_selection import modelling
from src.utils import utils
from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import Cluster
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

class model_training:
    def __init__(self):
        self.log=log()
        self.file_object=open("src/logs/training_logs/training_logs.txt","a+")
        self.loader=loader()
        self.preprocessor=preprocessor()
        self.database=database()
        self.model=modelling()
        self.utils=utils(file_obejct=self.file_object,log=self.log)




    def training(self):
        try:
           self.log.log(self.file_object,"model training started!!")
           self.log.log(self.file_object, "Cassandra Database Building started!!")
           df=self.database.data_load()
           columns,data_type=self.database.extract_columns_and_datatype(data=df)
           print(columns,data_type)
           print(len(columns),len(data_type))
           self.database.database_table_creation(columns=columns,data_type=data_type)
           self.database.database_inserion(data=df,columns=columns)
           self.database.extract_data_form_database_into_lacal(columns=columns)
           self.log.log(self.file_object, "Cassandra Database Building completed!!")
           self.log.log(self.file_object,"Dataset loading Started!!")
           data=self.loader.load()
           self.log.log(self.file_object, "Dataset loading completed!!")
           self.log.log(self.file_object, "Data Preprocessing Started!!")
           data=self.preprocessor.change_column_name(data)
           data=self.preprocessor.outlier_removal(data)
           data=self.preprocessor.skewness_removal(data)
           df=self.preprocessor.drop_unnecessary_columns(data)
           X=df.drop(columns=['credit_risk'])
           Y=df['credit_risk']
           x,y=self.preprocessor.over_sampling_operation(features=X,label=Y)
           print(x,y)
           #x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20,random_state=42)
           #print(x_train,y_train,x_test,y_test)
           #grad=GradientBoostingClassifier()
           #grad.fit(x_train,y_train)
           #p=grad.predict(x_test)
           #print(accuracy_score(y_test,p))
           #self.log.log(self.file_object, "Data Preprocessing Completed!!")
           #self.log.log(self.file_object, "modelling using ML algorithms started!!")
           #model_name,model_object=self.model.best_model_selection(x_train=x_train,y_train=y_train,x_test=x_test,y_test=y_test)
           #self.log.log(self.file_object, "modelling Completed, Best model is selected i.e %s"%model_name)
           #self.utils.model_saver(model_name=model_name,model=model_object)
           #self.log.log(self.file_object, "model training Completed Successfully!!")

        except Exception as e:
            self.log.log(self.file_object,"exception occurred while model training : %s"%e)
            self.log.log(self.file_object,"model training unsuccessful")
            return e



train=model_training()
train.training()