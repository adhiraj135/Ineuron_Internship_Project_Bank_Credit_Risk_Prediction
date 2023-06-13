from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV
from src.logging import logging
from sklearn.metrics import accuracy_score



class modelling:
    def __init__(self):
        self.random=RandomForestClassifier()
        self.gradient=GradientBoostingClassifier()
        self.log=logging()
        self.file_object=open('F:/Inueron_Internship_Project_Prediction_Credit_Risk/src/logs/training_logs/model_logs.txt','a+')


    def model_fine_tuning_random_forest(self,x_train,y_train):
        self.log.log(self.file_object,"model fine tuning for random forest started")
        try:
            random_params = {
            'n_estimators':[i for i in range(10,500,50)],
            'max_depth':[i for i in range(2,20,2)],
            'min_samples_split':[i for i in range(2,20,2)],
            'min_samples_leaf':[i for i in range(2,10,2)],
            'max_features':["sqrt","log2"]
             }
            random_grid=GridSearchCV(estimator=self.random,param_grid=random_params,cv=5,verbose=3)
            random_grid.fit(x_train,y_train)

            n_estimators=random_grid.best_params_['n_estimators']
            max_depth=random_grid.best_params_['max_depth']
            min_samples_split=random_grid.best_params_['min_samples_split']
            min_samples_leaf=random_grid.best_params_['min_samples_leaf']
            max_features=random_grid.best_params_['max_features']

            best_random=RandomForestClassifier(n_estimators=n_estimators,max_depth=max_depth,min_samples_split=min_samples_split,min_samples_leaf=min_samples_leaf,max_features=max_features)
            self.log.log(self.file_object, "best param for random fores are" +"\t"+"max_depth : %s"%max_depth+"\t"+"n_estimators : %s"%n_estimators+"\t"+"min_samples_split : %s"%min_samples_split+"\t"+"min_samples_leaf : %s"%min_samples_leaf+"\t"+"max_features : %s"%max_features)
            self.log.log(self.file_object, "model fine tuning for random forest successful best parameters extracted")
            return best_random

        except Exception as e:
            self.log.log(self.file_object, "error in model fine tuning for random forest %s"%e)
            self.log.log(self.file_object, "model fine tuning for random forest is unsuccessful")
            return e


    def best_model_selection(self,x_train,y_train,x_test,y_test):
         self.log.log(self.file_object,"best model selection operation started")
         try:
             rf=self.model_fine_tuning_random_forest(x_train,y_train)
             rf.fit(x_train,y_train)
             rf_pred=rf.predict(x_test)
             rf_accuracy=accuracy_score(y_test,rf_pred)


             gb= GradientBoostingClassifier()
             gb.fit(x_train, y_train)
             gb_pred = gb.predict(x_test)
             gb_accuracy = accuracy_score(y_test, gb_pred)
             print(rf_accuracy,gb_accuracy)

             if rf_accuracy>gb_accuracy:
                self.log.log(self.file_object, "best model selected is random forest")
                return "Random Forest",rf
             elif rf_accuracy<gb_accuracy:
                self.log.log(self.file_object, "best model selected is gradient boosting")
                return "Gradient Boosting",gb
             self.log.log(self.file_object, "best model selection operation completed")

         except Exception as e:
             self.log.log(self.file_object, "error in best model selection : %s"%e)
             self.log.log(self.file_object, "best model selection unsuccessful")
             return e