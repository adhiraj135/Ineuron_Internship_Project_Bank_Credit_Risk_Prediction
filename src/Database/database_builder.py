from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import Cluster
import pandas as pd
import warnings
from src.logger import log
import csv
warnings.filterwarnings("ignore")

class database:
    def __init__(self):
        self.log = log()
        self.file = open('F:/Ineuron_Internship_Project_Bank_Credit_Risk_Prediction/src/logs/training_logs/database_logs.txt', 'a+')
        self.log.log(file_object=self.file,message="trying to connect the database")
        self.clientID = "kZxKjjtkNmGJHqtJMhmaMrIP"
        self.secret = "eGOE5khqAkvxMR+W_8hQdNx9dFM5pBMt8_bqC-pO6,XoPoTRoME6KxIovCDdq7wqtWW4MCr1EHNmkfpCJagNebrTlubxLo2c..FTScK_ypYPOQyekRD2kcOBiNSb_Hk3"
        self.cloud_config = {'secure_connect_bundle': "F:/Ineuron_Internship_Project_Bank_Credit_Risk_Prediction/secure-connect-creditriskdata.zip"}
        self.keyspace='credit_risk_data'
        self.table_name='bank_credit_data_table'
        self.path='F:/Ineuron_Internship_Project_Bank_Credit_Risk_Prediction/Dataset/SouthGermanCredit.asc'

    def data_load(self):
        self.log.log(file_object=self.file,message="data loading of the data to be stored in cassandra database started")
        try:
            df=pd.read_table(self.path,delimiter=' ')
            df.columns = ['status', 'duration', 'credit_history', 'purpose', 'amount', 'savings', 'employment_duration',
                          'installment_rate', 'personal_status_sex', 'other_debtors', 'present_residence', 'property',
                          'age', 'other_installment_plans',
                          'housing', 'number_credits', 'job', 'people_liable', 'telephone', 'foreign_worker',
                          'credit_risk']
            ID = list(df.index)
            df.insert(0,"ID",ID)
            df.to_csv('F:/Ineuron_Internship_Project_Bank_Credit_Risk_Prediction/Dataset/data.csv', header=True,index=False)
            self.log.log(file_object=self.file,message="data loading successfully completed")
            return df
        except Exception as e:
            self.log.log(file_object=self.file,message="error in data loading of the data to be stored in cassandra database %s"%e)
            self.log.log(file_object=self.file,message="data loading unsuccessful")
            return e

    def extract_columns_and_datatype(self,data):
        self.log.log(file_object=self.file,message="extraction columns and datatype from the data to be stored in cassandra started")
        try:
           columns=list(data.columns)
           data_type=[]
           data_type.append("int PRIMARY KEY")
           for i in range(len(data.dtypes.values)-1):
                data_type.append(str(data.dtypes.values[i]).split('64')[0])
           self.log.log(file_object=self.file,message="extraction columns and datatype from the data to be stored in cassandra is successful")
           return columns,data_type
        except Exception as e:
            self.log.log(file_object=self.file,message="error in extraction columns and datatype %s"%e)
            self.log.log(file_object=self.file,message="extraction columns and datatype from the data to be stored in cassandra is unsuccessful")
            return e

    def database_connection(self):
        self.log.log(file_object=self.file, message="database connection operation started")
        try:
            auth_provider = PlainTextAuthProvider(self.clientID, self.secret)
            cluster = Cluster(cloud=self.cloud_config, auth_provider=auth_provider)
            session = cluster.connect()
            self.log.log(file_object=self.file, message="database connection operation successful")
            return session
        except Exception as e:
            self.log.log(file_object=self.file, message="database connection operation %s"%e)
            self.log.log(file_object=self.file, message="database connection operation unsuccessful")
            return e




    def database_table_creation(self,columns,data_type):
        self.log.log(file_object=self.file,message="Cassandra database table creation started")
        try:
            session=self.database_connection()
            session.execute("USE {key_space_name};".format(key_space_name=self.keyspace))
            result=session.execute("SELECT COUNT(*) FROM system_schema.tables WHERE keyspace_name = 'credit_risk_data' AND table_name = 'bank_credit_data_table';")
            if result[0][0]==1:
                 session.shutdown()
                 self.log.log(file_object=self.file,message="Cassandra database table already created")
                 pass
            else:
                for i in range(len(columns)):
                    type=data_type[i]
                    column=columns[i]
                    print(column, type)
                    try:
                       session.execute("ALTER TABLE {table} ADD {column_name} {type}".format(table=self.table_name,column_name=column,type=type))
                    except:
                       session.execute("CREATE TABLE {table} ({column_name} {type})".format(table=self.table_name,column_name=column,type=type))
                session.shutdown()
                self.log.log(file_object=self.file, message="Cassandra database table successfully created")

        except Exception as e:
            self.log.log(file_object=self.file, message="Error in Cassandra database table creation %s"%e)
            self.log.log(file_object=self.file, message="Cassandra database table creation is unsuccessful")
            return e

    def database_inserion(self,data,columns):
        self.log.log(file_object=self.file, message="Cassandra database data insertion started")
        try:
            session=self.database_connection()
            session.execute("USE {key_space_name}".format(key_space_name=self.keyspace))
            table_rows = session.execute("SELECT count(*) FROM {table};".format(table=self.table_name))
            if len(data)==table_rows[0][0]:
                session.shutdown()
                self.log.log(file_object=self.file, message="Cassandra database table already contains the full data")
                pass
            else:
                with open('F:/Ineuron_Internship_Project_Bank_Credit_Risk_Prediction/Dataset/data.csv','r') as f:
                     next(f)
                     column_names= ','.join(columns)
                     reader=csv.reader(f,delimiter="\n")
                     for i in enumerate(reader):
                         for data in i[1]:
                             for cols in column_names.split("'"):
                                  session.execute("INSERT INTO {table} ({columns}) VALUES ({values});".format(table=self.table_name,columns=cols,values=data))
                session.shutdown()
                self.log.log(file_object=self.file, message="Cassandra database data insertion successful")
        except Exception as e:
            self.log.log(file_object=self.file, message="Error in Cassandra database data insertion %s"%e)
            self.log.log(file_object=self.file, message="Cassandra database data insertion unsuccessful")
            return e

    def extract_data_form_database_into_lacal(self,columns):
        self.log.log(file_object=self.file, message="Extract data from Cassandra database into lacal stared")
        try:
            session=self.database_connection()
            session.execute("USE {key_space_name}".format(key_space_name=self.keyspace))
            data = []
            for row in session.execute("select * from {table};".format(table=self.table_name)):
                data.append(row._asdict())
            df=pd.DataFrame(data,columns=columns)
            df.drop(columns=["ID"],inplace=True)
            df.to_csv("F:/Ineuron_Internship_Project_Bank_Credit_Risk_Prediction/Dataset/DATABASE_INPUT_FILE.csv",header=True,index=False)
            session.shutdown()
            self.log.log(file_object=self.file, message="Extraction of data from Cassandra database into lacal successful")
        except Exception as e:
            self.log.log(file_object=self.file, message="Error in Extraction of data from Cassandra database into lacal %s"%e)
            self.log.log(file_object=self.file, message="Extraction of data from Cassandra database into lacal unsuccessful")
            return e
