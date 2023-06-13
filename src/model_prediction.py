import os

from src.Data_Loader.loader import loader
from src.Feature_Engineering.preprocessing import preprocessor
from src.utils import utils
from src.logging import logging


class prediction:
    def __init__(self):
        self.log=logging()
        self.data_loader=loader()
        self.preprocessing=preprocessor()
        self.prediction_file_object=open('F:/Inueron_Internship_Project_Prediction_Credit_Risk/src/logs/prediction_logs/predicton_logs.txt','a+')
        self.model_path='F:/Inueron_Internship_Project_Prediction_Credit_Risk/src/saved_model'
        self.utils=utils(file_obejct=self.prediction_file_object,log=self.log)

    def prediction(self):
        self.log.log(self.prediction_file_object,"prediction on input data file created using inputs by the user on webpage started")
        try:
            self.log.log(self.prediction_file_object,"prediction data loading started!!")
            data=self.data_loader.prediction_data_loader()
            self.log.log(self.prediction_file_object, "prediction data loaded successfully!!")
            self.log.log(self.prediction_file_object, "prediction data preprocessig started!!")
            data=self.preprocessing.drop_unnecessary_columns_prediction(data)
            print(data.columns)
            self.log.log(self.prediction_file_object, "prediction data preprocessing completed successfully!!")
            self.log.log(self.prediction_file_object,"model Loading started!!")
            name=os.listdir(self.model_path)[0]
            model=self.utils.model_loader(model_name=name)
            self.log.log(self.prediction_file_object,"model : %s loaded successfully"%name)
            prediction=model.predict(data.values)
            d={
                1:"Good",
                0:"Bad"
            }
            return d[prediction[0]]

        except Exception as e:
            self.log.log(self.prediction_file_object,"error while prediction through model %s"%e)
            self.log.log(self.prediction_file_object,"model prediction unsuccessful")
            return e