from flask import Flask,render_template,request
from flask_cors import CORS,cross_origin
from src.Data_Loader.loader import loader
import pandas as pd
from src.model_prediction import prediction


application=Flask(__name__)
CORS(application)

@application.route('/',methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@application.route('/predict',methods=['GET','POST'])
@cross_origin()
def predict():
    try:
        if request.method=='POST':
            inputs=request.form
            values=[]
            load=loader()
            for i in inputs.values():
                values.append(i)
            df=load.load()
            pred_df=pd.DataFrame(values,index=df.drop(columns=['credit_risk']).columns).T
            pred_df.to_csv("Dataset/prediction_file.csv",header=True,index=False)
            pred=prediction()
            result=pred.prediction()
            #print(result)
            if result=='Bad':
                return render_template('result.html', result_text="Credit Risk is {prediction}, Loan Applicant is likely to Default".format(prediction=result))
            else:
                return render_template('result.html',result_text="Credit Risk is {prediction}, Loan Applicant is likely to repay the credit obligations".format(prediction=result))
    except Exception as e:
        return e


if __name__=="__main__":
    application.run(host='0.0.0.0',port=8080)
