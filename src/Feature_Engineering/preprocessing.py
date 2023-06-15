from src.logger import log
import numpy as np
from imblearn.over_sampling import SMOTE


class preprocessor:
    def __init__(self):
        self.log=log()
        self.file_object=open('src/logs/training_logs/preprocessing_log.txt','a+')
        self.prediction_file_object = open('src/logs/prediction_logs/preprocessing_log.txt', 'a+')


    def change_column_name(self,data):
        self.log.log(self.file_object, "column name changing preprocessing started")
        try:
            data.columns=['status', 'duration', 'credit_history', 'purpose', 'amount', 'savings', 'employment_duration',
            'installment_rate', 'personal_status_sex', 'other_debtors', 'present_residence', 'property', 'age', 'other_installment_plans',
            'housing', 'number_credits', 'job', 'people_liable', 'telephone', 'foreign_worker', 'credit_risk']
            self.log.log(self.file_object,"column names successfully changed")
            return data
        except Exception as e:
            self.log.log(self.file_object, "exception occurred while changing column names operation : %s" % e)
            self.log.log(self.file_object, "column names successfully changed")
            raise e

    def outlier_removal(self,data):
        self.log.log(self.file_object, "outlier removal preprocessing started")
        try:
            for col in data.columns:
                q25 = data[col].quantile(0.25)
                q75 = data[col].quantile(0.75)
                IQR = q75 - q25
                lower_limit = q25 - (1.5) * (IQR)
                upper_limit = q75 + (1.5) * (IQR)
                data.loc[data[col] < lower_limit, col] = lower_limit
                data.loc[data[col] > upper_limit, col] = upper_limit

            self.log.log(self.file_object,"upper level outliers has been replaced with upper_limit derived through IQR and similarly lower level outliers replaced with lower_limit")
            return data
        except Exception as e:
            self.log.log(self.file_object, "exception occurred while outlier removal operation : %s" % e)
            self.log.log(self.file_object,"outlier removal unssucessful")
            raise e

    def skewness_removal(self,data):
        self.log.log(self.file_object, "skewness removal preprocessing started")
        try:
            right_skewed_columns = data.skew()[(data.skew() > 0.5)].index
            for col in right_skewed_columns:
                data[col]=np.log(data[col]+1)

            left_skewed_columns = data.skew()[(data.skew() < -0.5)].index
            for cols in left_skewed_columns:
                data[cols]=np.square(data[cols])
            self.log.log(self.file_object,"right skewness and left skewness removal successful")
            return data
        except Exception as e:
            self.log.log(self.file_object, "exception occurred while skewness removal operation : %s" % e)
            self.log.log(self.file_object, "right skewness and left skewness removal unsuccessful")
            raise e

    def drop_unnecessary_columns(self,data):
        self.log.log(self.file_object, "dropping unnecessary column preprocessing started")
        try:
            columns_to_remove = ['other_debtors', 'other_installment_plans', 'people_liable', 'foreign_worker', 'job',
                                 'housing']
            data.drop(columns=columns_to_remove,inplace=True)
            self.log.log(self.file_object,"Columns which are not relevant dropped successfully")
            return data

        except Exception as e:
            self.log.log(self.file_object, "exception occurred while dropping columns operation : %s" % e)
            self.log.log(self.file_object,"dropping unnecessary columns unsuccessful")
            raise e

    def over_sampling_operation(self,features,label):
        self.log.log(self.file_object, "oversampling minority class preprocessing started")
        try:
            smote=SMOTE()
            x,y=smote.fit_resample(features,label)
            self.log.log(self.file_object,"oversampling operation minority class successful")
            return x,y
        except Exception as e:
            self.log.log(self.file_object, "exception occurred while oversampling operation : %s" %e)
            self.log.log(self.file_object,"oversampling operation unsuccessful")
            raise e

    def drop_unnecessary_columns_prediction(self,data):
        self.log.log(self.prediction_file_object, "dropping unnecessary column preprocessing started")
        try:
            columns_to_remove = ['other_debtors', 'other_installment_plans', 'people_liable', 'foreign_worker', 'job',
                                 'housing']
            data.drop(columns=columns_to_remove,inplace=True)
            self.log.log(self.prediction_file_object,"Columns which are not relevant dropped successfully")
            return data

        except Exception as e:
            self.log.log(self.prediction_file_object, "exception occurred while dropping columns operation : %s" % e)
            self.log.log(self.prediction_file_object,"dropping unnecessary columns unsuccessful")
            raise e
