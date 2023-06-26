import pyodbc
import config
import pandas as pd

class DB_connection:
    def connect_db(self, pwd):
        driver = config.DRIVER
        server = config.SERVER
        database = config.DATABASE
        uid = config.UID
        pwd = pwd
        trust = config.TRUST
        con_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={uid};PWD={pwd}'
        cnxn = pyodbc.connect(con_string)
        cnxn.autocommit =  True
        cursor = cnxn.cursor()
        print("Connection Succesfull with DB")
        return cnxn

    def fetch_data(self, cnxn):
        query = 'Select top 10 * From SALES'
        print (query)
        df = pd.read_sql(query, cnxn)
        return df

    def get_data(self, cnxn):
        df = self.fetch_data(cnxn)
        return df.to_dict('r')
