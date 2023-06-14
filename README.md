# **Internship-South-German-Bank-Credit-Risk**

## **Table of Content**

1. Introduction
2. Approach
3. User Interface
4. Deployment Link
5. Installation
6. Technology Used
7. Document

## **Introduction**

Normally, most of the bank's wealth is obtained from providing credit loans so that a marketing bank must be able to reduce the risk of non-performing credit loans. The risk of providing loans can be minimized by studying patterns from existing lending data. One technique that you can use to solve this problem is to use data mining techniques. Data mining makes it possible to find hidden information from large data sets by way of classification. The goal of this project, you have to build a model to predict whether the person, described by the attributes of the dataset, is a good (1) or a bad (0) credit risk

**Input variables are:**

laufkont = status
laufzeit = duration
moral = credit_history
verw = purpose
hoehe = amount
sparkont = savings
beszeit = employment_duration
rate = installment_rate
famges = personal_status_sex
buerge = other_debtors
wohnzeit = present_residence
verm = property
alter = age
weitkred = other_installment_plans
wohn = housing
bishkred = number_credits
beruf = job
pers = people_liable
telef = telephone
gastarb = foreign_worker

**Output variables:**

kredit = credit_risk

## **Approach**

Data Exploration : I started exploring dataset using pandas,numpy,matplotlib and seaborn.

Data visualization : Ploted graphs to get insights about dependend and independed variables.

Feature Engineering : All The Value Are Arrange In One Range.

Model Selection I : Tested all base models to check the base accuracy.

Model Selection II : Performed Hyperparameter tuning using gridsearchCV.

Pickle File : Selected model as per best accuracy and created pickle file using Pickle .

Webpage & deployment : 
1. Created a web form that takes all the necessary inputs from user and shows output. 
2. Deploy 

## **User Interface**

The Prediction of Credit Risk Final Model Run in Local Enviornment

**Main Page :**

![credit_risk1 png](https://github.com/adhiraj135/Ineuron_Internship_Project_Bank_Credit_Risk_Prediction/assets/107035869/bce64629-f65b-46e3-80ec-51f7cf8a8570)

**result page :**

![credit_risk3](https://github.com/adhiraj135/Ineuron_Internship_Project_Bank_Credit_Risk_Prediction/assets/107035869/a8e71a06-b159-48a1-a35b-a187829fa4b0)



## **Deployment Link**

AWS - [http://creditriskpredictionapp-env.eba-7zpp7qij.us-east-2.elasticbeanstalk.com/]()

**Installtion**

The Code is written in Python 3.8.11. If you don't have Python installed you can find it your link here. If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after cloning the repository.

1. Create a Virtual Env with conda create "Your Env name"
2. pip install -r requirements.txt
3. Run app.py file

## **Technology Used**

1. Python
2. Sklearn
3. Pandas
4. Numpy
5. Flask
6. HTML
7. CSS
8. Cassendra
9. AWS

## **Document**

Below providing the link of all the document that are required for creating the project.

Link: https://github.com/adhiraj135/Ineuron_Internship_Project_Bank_Credit_Risk_Prediction/tree/master/Documents
