import pandas as pd
from src.logging import logging


class loader:
    def __init__(self):
        self.path='F:\Inueron_Internship_Project_Prediction_Credit_Risk\Dataset\DATABASE_INPUT_FILE.csv'
        self.prediction_path='F:\Inueron_Internship_Project_Prediction_Credit_Risk\Dataset\prediction_file.csv'
        self.file=open('F:/Inueron_Internship_Project_Prediction_Credit_Risk/src/logs/training_logs/data_loader_log.txt',"a+")
        self.log=logging()
        self.prediction_file_object=open('F:/Inueron_Internship_Project_Prediction_Credit_Risk/src/logs/prediction_logs/prediction_data_loader_log.txt','a+')

    def load(self):
        self.log.log(self.file, "data loading started")
        try:
            df=pd.read_csv(self.path)
            self.log.log(self.file,"data successfully loaded")
            return df

        except Exception as e:
            self.log.log(self.file,"exception occurred while data loading: %s" %e)
            self.log.log(self.file,"data loading unsuccessful")
            return e

    def prediction_data_loader(self):
        self.log.log(self.prediction_file_object,"prediction data which was created using the input by users on webpage operation started")
        try:
            pred_df=pd.read_csv(self.prediction_path)
            self.log.log(self.prediction_file_object, "prediction data successfully loaded")
            return pred_df
        except Exception as e:
            self.log.log(self.file, "error in prediction data laoding : %s"%e)
            self.log.log(self.file, "prediction data loading is unsuccessful")
            return e



